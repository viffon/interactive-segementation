import cv2
import numpy as np


class GrowCut:

    def __init__(self, image, strength, mask, iteration):
        self.image = image
        self.strength = strength
        self.mask = mask
        self.iteration = iteration

    @staticmethod
    def g(cp, cq):
        return 1 - abs(int(cp) - int(cq)) / 255

    def grow_cut(self):
        height, width = self.image.shape[:2]
        changes = 1
        n = 0
        # Von Neumann neighborhood
        # neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # Moore neighborhood
        neighbors = [(-1, -1), (1, 1), (-1, 1), (1, -1), (-1, 0), (1, 0), (0, 1), (0, -1)]
        state_next = self.strength.copy()
        label_next = self.mask.copy()
        while changes > 0 and n < self.iteration:
            changes = 0
            n += 1
            for j in range(width):
                for i in range(height):
                    c_p = self.image[i, j]
                    s_p = self.strength[i, j]
                    for neighbor in neighbors:
                        dr, dc = neighbor
                        row = i + dr
                        col = j + dc
                        if 0 <= row < height and 0 <= col < width:
                            c_q = self.image[row, col]
                            s_q = self.strength[row, col]

                            gc = self.g(c_q, c_p)
                            # print(gc)

                            if gc * s_q > s_p:
                                state_next[i, j] = gc * s_q
                                # print(state_next[i, j])
                                label_next[i, j] = self.mask[row, col]

                                changes += 1
            self.strength = state_next
            self.mask = label_next

        return self.mask
