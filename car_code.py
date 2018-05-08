import cv2
import os
import numpy as np

# 1 转换了灰度化
img = cv2.imread(os.getcwd()+"/car/car.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("1", img_gray)

# 2 Sobel
gradX = cv2.Sobel(img_gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(img_gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)
cv2.imshow("2", gradient)

# 3
blurred = cv2.blur(gradient, (9, 9))
(_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)
cv2.imshow("3", thresh)

# 4
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow("4", closed)
#ddff
print("测试GIT使用")
# 5
closed = cv2.erode(closed, None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)
cv2.imshow("5", closed)

# 6
(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

# compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))

# draw a bounding box arounded the detected barcode and display the image
cv2.drawContours(img, [box], -1, (0, 255, 0), 3)
cv2.imshow("6", img)




# 2、将灰度图像二值化，设定阈值是100
img_thre = img_gray

cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY, img_thre)
#cv2.imshow('2', img_thre)

img_edge = cv2.Canny(img_thre, 100, 200)
#cv2.imshow("3", img_edge)

# cnts = cv2.findContours(img_edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
# rect = cv2.minAreaRect(c)
# box = np.int0(cv2.cv2.BoxPoints(rect))
# cv2.drawContours(img, [box], -1, (0, 255, 0), 3)
# cv2.imshow("Image", img)


cv2.waitKey(0)

