import cv2 as cv

img = cv.imread(r"D:\master\opencv-python\image\back.jpg", 0)
cv.imshow("img", img)
ret, thre1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
print("阈值为" + str(ret))
cv.imshow("thre1", thre1)
adaptive_thre1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                      cv.THRESH_BINARY, 7, 2)
adaptive_thre2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv.THRESH_BINARY, 7, 2)
cv.imshow("adaptive_thre1", adaptive_thre1)
cv.imshow("adaptive_thre2", adaptive_thre2)
cv.waitKey()
cv.destroyAllWindows()
