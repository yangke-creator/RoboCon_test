"""
    思路：
    1.先是读取图片，再copy一份来进行比较
    2.将图片转换为HSV格式，设置黄色的HSV阈值
    3.阈值提取黄色赛道，将获得的二值化图片用于轮廓检测
    4.找到最大的轮廓并绘制
    5.显示原图和处理后的图片
    必做题应该差不多就这样吧
"""
import cv2 as cv
import numpy as np

img = cv.imread('saidao.jpeg')
# cap = cv.VideoCapture(0)

# ret, img = cap.read()
# 创建原图进行对比
img_org = img.copy()
# cv.imshow('img', img)
# HSV转换
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)
lower_yellow = np.array([6, 111, 85])
upper_yellow = np.array([21, 255, 255])
# 设置hsv阈值提取黄色
mask = cv.inRange(hsv, lower_yellow, upper_yellow)
# mask与img按位与运算
# res = cv.bitwise_and(img, img, mask=mask)
contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# 判断是否有轮廓
if len(contours) != 0:
    # 找到最大轮廓
    max_contour = max(contours, key=cv.contourArea)
    # 绘制轮廓
    cv.drawContours(img, [max_contour], -1, (0, 0, 255), 3)
cv.imshow('img_org', img_org)
cv.imshow('img', img)
# cv.imshow('mask', mask)
# cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()