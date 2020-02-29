import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import random
import math

img = cv.imread(r"D:\master\opencv-python\image\cat2.jpg")
img_bilateral = cv.bilateralFilter(img,0,0.2,40)

cv.imshow("img",img)
cv.imshow("img_bilateral",img_bilateral)
cv.waitKey(0)
cv.destroyAllWindows()