import cv2 as cv

img = cv.imread("sad.jpg", 1)  # 读取图片
cv.imshow('input image', img)  # 显示图片
pixel = img[100, 100]
shape = img.shape
size = img.size
data = {
    "pixel:100,100": pixel[0],
    "shape": shape,
    # 高、宽、通道
    "size": size
    # 高*宽*通道
}
for key in data:
    print(str(key) + ':' + str(data[key]))
    print('*' * 25)
roi = img[100:515, 100:696]  # 高，宽
constant = cv.copyMakeBorder(roi, 5, 5, 5, 5, cv.BORDER_CONSTANT, value=[0, 255, 0]) 
# 添加绿色边框
cv.imwrite("test.jpg", constant)  # 保存图片
cv.imshow("test.jpg", constant)
cv.waitKey()

cv.destoryAllWindows()
