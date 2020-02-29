import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"D:\master\opencv-python\image\hrzq.jpg")
img_cvt = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,img_thr = cv.threshold(img_cvt,200,255,cv.THRESH_BINARY_INV)
kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,5))
print(kernel)
open = cv.morphologyEx(img_thr,cv.MORPH_OPEN,kernel,iterations=1)
close = cv.morphologyEx(img_thr,cv.MORPH_CLOSE,kernel,iterations=1)
gradient = cv.morphologyEx(img_thr,cv.MORPH_GRADIENT,kernel,iterations=1)
tophat = cv.morphologyEx(img_thr,cv.MORPH_TOPHAT,kernel,iterations=1)
blackhat = cv.morphologyEx(img_thr,cv.MORPH_BLACKHAT,kernel,iterations=1)

images=[img_thr,open,close,gradient,tophat,blackhat]
titles=["img_thr","open","close","gradient","tophat","blackhat"]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),    plt.yticks([])
plt.show()

# 　　开运算：先进行腐蚀操作，后进行膨胀操作，主要用来去除一些较亮的部分，即先腐蚀掉不要的部分，再进行膨胀。

# 　　闭运算：先进行膨胀操作，后进行腐蚀操作，主要用来去除一些较暗的部分。

# 　　形态学梯度：膨胀运算结果减去腐蚀运算结果，可以拿到轮廓信息。

# 　　顶帽运算：原图像减去开运算结果。

# 　　底帽运算：原图像减去闭运算结果。