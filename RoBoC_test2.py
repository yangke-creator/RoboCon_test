"""
    思路：
    1.先做完必做题，获得赛道轮廓
    2.查找赛道中线
    3.进行路径规划，符合“尽可能快地到达终点，尽可能向前移动”
        我的路径规划思路是：前期向右移动多一点，后期向前移动多一点
    4.显示原图和处理后的图片（包括路径）
"""

import cv2 as cv
import numpy as np

point1 = 100     # 相距中线100像素
point2 = 50      # 相距中线50像素
direction = []   # 运动方向
pos_org = (100, 300) # 初始位置

# 查找赛道中线
def find_line(mask):
    line = {}
    for y in range(mask.shape[0]):
        pixels = np.where(mask[y, :] > 0)[0]
        if len(pixels) > 0:   # 判断是否有赛道
            line[y] = int((pixels[0] + pixels[-1]) / 2)  # 计算中点
    return line         # 返回赛道中线字典

def move_robot(pos_org, line,step=10, thr=5):
    global point1, point2
    global direction
    path = [pos_org]    # 运动路径
    x, y  = pos_org     # 移动到的位置
    cnt = 0       # 移动次数
    while cnt < 200:
        if y in line.keys():   #判段y是否在赛道中线字典中
            x_line = line[y]   # 赛道中线x坐标
            distence = abs(x - x_line)
            if distence < thr:
                break
            elif distence >= point1:
                direction = [False, False, True]  # 右右前
            elif point2 <= distence < point1:
                direction = [False, True] # 右前
            elif distence < point2:
                direction = [False, True, True] # 右前前
        else:
            direction = [True] # 前
        for d in direction:
            if d == True: # 向前
                y -= step
            else:
                x += step # 向右
                distence = abs(x - x_line)
                if distence < thr:
                    path.append((x, y))
                    break
            path.append((x, y))
        cnt += 1
    return path


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

line = find_line(mask)
for y, x in line.items():
    cv.circle(img, (x, y), 2, (0, 0, 255), -1)      # 绘制赛道中线

path = move_robot(pos_org, line)

for i in range(len(path) - 1):                            
    cv.line(img, path[i], path[i + 1], (255, 0, 0), 3)  # 绘制路径
    cv.circle(img, path[i], 3, (0, 0, 255), -1)         # 绘制路径点
    cv.circle(img, path[i + 1], 3, (0, 0, 255), -1)     # 绘制路径点

cv.circle(img, pos_org, 8, (0, 0, 255), -1)         # 绘制起始点
cv.circle(img, path[-1], 8, (255, 0, 0), -1)        # 绘制终点

cv.imshow('img_org', img_org)
cv.imshow('img', img)
cv.imwrite('img2.png', img)
# cv.imshow('mask', mask)
# cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()