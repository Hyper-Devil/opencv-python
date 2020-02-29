import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread(r"D:\master\opencv-python\image\front.jpg")
img_gauss = cv.GaussianBlur(img, (3, 3), 1)
cv.imshow("img", img)
cv.imshow("img_gauss", img_gauss)
cv.waitKey(0)
cv.destroyAllWindows()
