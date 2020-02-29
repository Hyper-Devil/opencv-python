import cv2
import matplotlib.pyplot as plt
import numpy as np

img2 = cv2.imread(r'D:\master\opencv-python\image\sudoku.jpg')
img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)  # matplotlib的图像为RGB格式
rows, cols, ch = img.shape

pts1 = np.float32([[223, 490], [563, 455], [186, 847], [577, 848]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], 
 [300, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (300, 300))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
