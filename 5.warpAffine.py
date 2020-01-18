import cv2 as cv
import numpy as np

img = cv.imread(r"D:\master\opencv-python\image\sad.jpg")
cv.imshow("img", img)
rows, cols = img.shape[0:2]

M_tran = np.float32([[1, 0, 100], [0, 1, 50]])  # 向右平移100，向下平移50
img_trans = cv.warpAffine(img,
                          M_tran, (cols, rows),
                          borderValue=(255, 255, 255))
#? dsize反过来了
cv.imshow("trans", img_trans)

M_enlarge = np.float32([[0.5, 0, 0], [0, 2, 0]])  # 水平方向放大了0.5倍，竖直方向放大了2倍
img_enlarge = cv.warpAffine(img,
                            M_enlarge, (cols, rows),
                            borderValue=(255, 255, 255))
cv.imshow("enlarge", img_enlarge)

# *通过三点计算M阵的方法
pts1 = np.float32([[100, 100], [10, 20], [30, 6]])  ## 水平方向放大了2倍，竖直方向放大了0.5倍
pts2 = np.float32([[200, 50], [20, 10], [60, 3]])
M_cal = cv.getAffineTransform(pts1, pts2)
img_cal = cv.warpAffine(img,
                        M_cal, (cols * 2, int(rows * 0.5)),
                        borderValue=(255, 255, 255))
cv.imshow("cal", img_cal)

cv.waitKey()
cv.destroyAllWindows()
