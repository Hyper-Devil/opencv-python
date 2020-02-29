import cv2
import numpy as np

filename = 'D:\master\opencv-python\image\sad.jpg'
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# print(image)
cv2.imshow('origin', image)

h, w = image.shape[:2]  # 把图片2像素的行数，列数以及通道数返回给rows，cols，channels
sum = np.zeros((h + 1, w + 1), dtype=np.float32)  # 创建指定大小的数组，数组元素以 0 来填充：
imageIntegral = cv2.integral(image, sum, cv2.CV_32FC1)  # 计算积分图,输出是sum
result = np.zeros((h + 1, w + 1), dtype=np.uint8)
cv2.normalize(imageIntegral, result, 0, 255, cv2.NORM_MINMAX,
              cv2.CV_8UC1)  # 归一化处理
cv2.imshow("Image", result)
# cv2.imwrite("D:/Car_Identify/papers_for_edge/integral_result.jpg", result)![在这里插入图片描述](https://img-blog.csdnimg.cn/20190606180108399.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2ExNTIwNjA4NzAxMw==,size_16,color_FFFFFF,t_70)
cv2.waitKey()

