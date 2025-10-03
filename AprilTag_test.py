import pupil_apriltags as apriltags
import cv2 as cv

# Apriltag家族命名：tag36h11, tag25h9

# img = cv.imread("bac8ed8abb1f4efd83c3dd4e9aa57b7c.png", 0)
detector = apriltags.Detector(families='tag36h11') # 指定Apriltag家族为tag36h11
detector2 = apriltags.Detector(families='tag25h9') # 指定Apriltag家族为tag25h9
cap = cv.VideoCapture(0)
while True:
    ret, img = cap.read()
    img_org = img.copy()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    result = detector.detect(img)
    if len(result) == 0:
        result = detector2.detect(img)
    for r in result:
        # 获取四个角点的坐标
        a = (tuple(r.corners[0].astype(int))[0], tuple(r.corners[0].astype(int))[1])
        b = (tuple(r.corners[1].astype(int))[0], tuple(r.corners[1].astype(int))[1])
        c = (tuple(r.corners[2].astype(int))[0], tuple(r.corners[2].astype(int))[1])
        d = (tuple(r.corners[3].astype(int))[0], tuple(r.corners[3].astype(int))[1])
        cv.circle(img_org, a, 4, (0, 0, 255), -1)
        cv.circle(img_org, b, 4, (0, 0, 255), -1)
        cv.circle(img_org, c, 4, (0, 0, 255), -1)
        cv.circle(img_org, d, 4, (0, 0, 255), -1)
        cv.line(img_org, a, b, (0, 0, 255), 2)
        cv.line(img_org, b, c, (0, 0, 255), 2)
        cv.line(img_org, c, d, (0, 0, 255), 2)
        cv.line(img_org, d, a, (0, 0, 255), 2)
    print(result)
    cv.imshow('img_org', img_org)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
cap.release()
