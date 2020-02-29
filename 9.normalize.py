import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread(r"D:\master\opencv-python\image\back.jpg")
img_norm=cv.normalize(img,dst=None,alpha=350,beta=10,norm_type=cv.NORM_MINMAX)
cv.imshow("img",img)
cv.imshow("img_norm",img_norm)
cv.waitKey(0)
cv.destroyAllWindows()