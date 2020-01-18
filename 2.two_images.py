import cv2 as cv

img1 = cv.imread(r"D:\master\opencv-python\image\front.jpg")
high, weigh = img1.shape[0:2]
img2 = cv.imread(r"D:\master\opencv-python\image\back.jpg")
img2_roi = img2[0:high, 0:weigh]
result = cv.addWeighted(img1, 0.8, img2_roi, 0.2, 0)
cv.imshow("result", result)
cv.waitKey()
cv.destroyAllWindows()
