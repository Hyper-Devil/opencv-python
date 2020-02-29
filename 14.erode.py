import cv2 as cv

img = cv.imread(r"D:\master\opencv-python\image\hrzq.jpg")
img_cvt = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,img_thr = cv.threshold(img_cvt,200,255,cv.THRESH_BINARY_INV)
kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,5))
dst = cv.erode(img_thr,kernel,iterations=1)

cv.imshow("img",img)
cv.imshow("img_thr",img_thr)
cv.imshow("dst",dst)
cv.waitKey(0)
cv.destroyAllWindows()