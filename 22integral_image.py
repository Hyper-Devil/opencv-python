import cv2
import numpy as np
import matplotlib.pyplot as plt
import time


#获取积分图像
def integral(img):
    #积分图像比原始图像多一行一列，积分图像第一行第一列为0
    integimg = np.zeros(shape=(img.shape[0] + 1, img.shape[1] + 1),
                        dtype=np.int32)
    for i in range(1, img.shape[0]):
        for j in range(1, img.shape[1]):
            integimg[i][j] = img[i][j] + integimg[i - 1][j] + integimg[i][
                j - 1] - integimg[i - 1][j - 1]
    # plt.imshow( integimg )
    # plt.show()
    print('Done!')
    return integimg

if __name__ == '__main__':
    start = time.time()
    img = cv2.imread(r'D:\master\opencv-python\image\sad.jpg', cv2.IMREAD_GRAYSCALE)
    if (img is None):
        print('Not read img.')
    integimg = integral(img)
    # cv2.integral(img)
    end = time.time()
    print('程序用时：' + str(end - start) + '秒')
    