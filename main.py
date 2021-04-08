# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import numpy as np
from growcut import GrowCut
# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    img = cv2.imread('black-cat.jpg', 0)
    strength = np.zeros_like(img, np.float16)
    mask = np.zeros_like(img)
    strength[2:5, 1:80] = 1.0
    mask[2:5, 1:80] = 100
    strength[2:100, 155:160] = 1.0
    mask[2:100, 155:160] = 100

    strength[35:80, 100:105] = 1.0
    mask[35:80, 100:105] = 200
    mask[105, 50:90] = 200
    strength[105, 50:90] = 1.0
    #cv2.imshow('res.jpg', img)
    gc = GrowCut(img, strength, mask, 200)
    res = gc.grow_cut()
    #cv2.imshow('res.jpg', img)

    cv2.imshow('label.jpg', res)
    cv2.waitKey(0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
