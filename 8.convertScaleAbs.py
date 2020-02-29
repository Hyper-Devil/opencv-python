import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# img = cv.imread(r"D:\master\opencv-python\image\back.jpg")
# print(img)
# img_bright = cv.convertScaleAbs(img,alpha=1.5,beta=0)
# print(img_bright)

#* cv2.convertScaleAbs(src,alpha,beta)
#*     src: 图像对象矩阵
#* 　　 dst:输出图像矩阵
#*     alpha:y=ax+b中的a值
#*     beta:y=ax+b中的b值
#*     (对于计算后大于255的像素值会截断为255) 

img = cv.imread(r"D:\master\opencv-python\image\back.jpg")
a=1.5
b=0
y = np.float(a)*img+b
y[y>255]=255
y = np.round(y)
img_bright= y.astype(np.uint8)

cv.imshow("img",img)
cv.imshow("img_bright",img_bright)
cv.waitKey(0)
cv.destroyAllWindows()