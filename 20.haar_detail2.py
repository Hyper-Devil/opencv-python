import cv2
import numpy as np
import matplotlib.pyplot as plt


#
#计算积分图
#
def integral(img):
    integ_graph = np.zeros((img.shape[0], img.shape[1]), dtype=np.int32)
    for x in range(img.shape[0]):
        sum_clo = 0
        for y in range(img.shape[1]):
            sum_clo = sum_clo + img[x][y]
            integ_graph[x][y] = integ_graph[x - 1][y] + sum_clo
    return integ_graph


# Types of Haar-like rectangle features
#   --- ---
# |   |   |
# | - | + |
# |   |   |
# --- ---
#
#就算所有需要计算haar特征的区域
#
def getHaarFeaturesArea(width, height):
    widthLimit = width - 1
    heightLimit = height / 2 - 1
    features = []
    for w in range(1, int(widthLimit)):
        for h in range(1, int(heightLimit)):
            wMoveLimit = width - w
            hMoveLimit = height - 2 * h
            for x in range(0, wMoveLimit):
                for y in range(0, hMoveLimit):
                    features.append([x, y, w, h])
    return features


#
#通过积分图特征区域计算haar特征
#
def calHaarFeatures(integral_graph, features_graph):
    haarFeatures = []
    for num in range(len(features_graph)):
        #计算左面的矩形区局的像素和
        haar1 = integral_graph[features_graph[num][0]][features_graph[num][1]]-\
        integral_graph[features_graph[num][0]+features_graph[num][2]][features_graph[num][1]] -\
        integral_graph[features_graph[num][0]][features_graph[num][1]+features_graph[num][3]] +\
        integral_graph[features_graph[num][0]+features_graph[num][2]][features_graph[num][1]+features_graph[num][3]]
        #计算右面的矩形区域的像素和
        haar2 = integral_graph[features_graph[num][0]][features_graph[num][1]+features_graph[num][3]]-\
        integral_graph[features_graph[num][0]+features_graph[num][2]][features_graph[num][1]+features_graph[num][3]] -\
        integral_graph[features_graph[num][0]][features_graph[num][1]+2*features_graph[num][3]] +\
        integral_graph[features_graph[num][0]+features_graph[num][2]][features_graph[num][1]+2*features_graph[num][3]]
        #右面的像素和减去左面的像素和
        haarFeatures.append(haar2 - haar1)
    return haarFeatures


img = cv2.imread(r"D:\master\opencv-python\image\sad.jpg", 0)
integeralGraph = integral(img)
featureAreas = getHaarFeaturesArea(img.shape[0], img.shape[1])
haarFeatures = calHaarFeatures(integeralGraph, featureAreas)
print(haarFeatures)