import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
                
img = cv.imread(r"D:\master\opencv-python\image\back.jpg",0)

hist = cv.calcHist([img],[0],None,[256],[0,256])

plt.subplot(1,3,1),plt.plot(hist,color="r"),plt.axis([0,256,0,np.max(hist)])
plt.xlabel("gray level")
plt.ylabel("number of pixels")

plt.subplot(1,3,2),plt.hist(img.ravel(),bins=256,range=[0,256]),plt.xlim([0,256])
plt.xlabel("gray level")
plt.ylabel("number of pixels")

plt.subplot(1,3,3)
plt.plot(hist,color="r"),plt.axis([0,256,0,np.max(hist)])
plt.hist(img.ravel(),bins=256,range=[0,256]),plt.xlim([0,256])
plt.xlabel("gray level")
plt.ylabel("number of pixels")

plt.show()