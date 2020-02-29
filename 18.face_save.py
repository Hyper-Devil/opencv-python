import cv2
import numpy as np
from PIL import Image
import os

detector = cv2.CascadeClassifier(
    r'C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'
)
Id = input('enter your id:')
sampleNum = 0
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, img = cap.read()
    # print(ret)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.1, 3)
    print(faces)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 增加例子数
        sampleNum = sampleNum + 1
        # 把照片保存到数据集文件夹
        cv2.imwrite("dataSet/user." + str(Id) + '.' + str(sampleNum) + ".jpg",
                    gray[y:y + h, x:x + w])

        cv2.imshow('camera', img)whd


    if cv2.waitKey(100) == 27:  # press 'ESC' to quit
        break
    elif sampleNum > 20:
        break

cap.release()
cv2.destroyAllWindows()