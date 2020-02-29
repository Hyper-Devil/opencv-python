import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread(r"D:\master\opencv-python\image\back.jpg")
img_blur = cv.blur(img,(3,5))
# img_blur = cv.boxFilter(img,-1,(3,5))
cv.imshow("img",img)
cv.imshow("img_blur",img_blur)
cv.waitKey(0)
cv.destroyAllWindows()