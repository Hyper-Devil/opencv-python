import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import random

img = cv.imread(r"D:\master\opencv-python\image\sad.jpg")
rows, cols = img.shape[:2]

#加入椒盐噪声
for i in range(100):
    r = random.randint(0, rows - 1)
    c = random.randint(0, cols - 1)
    img[r, c] = 255

img_medianblur = cv.medianBlur(img, 5)

cv.imshow("img", img)
cv.imshow("img_medianblur", img_medianblur)
cv.waitKey(0)
cv.destroyAllWindows()