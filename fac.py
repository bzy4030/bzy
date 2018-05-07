# -*- coding: utf-8 -*-
import face_recognition
import cv2
import sys
import os
def face_reg(file):
    print("开始识别")
    # 读取图片并识别人脸
    img = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(img)
    print(face_locations)

    # 调用opencv函数显示图片
    img = cv2.imread(file)
    # 打开图框
    cv2.imshow("oldImage", img)

    # 遍历每个人脸，并标注
    faceNum = len(face_locations)
    for i in range(0, faceNum):
        # 绘制人脸位置
        top =  face_locations[i][0]
        right =  face_locations[i][1]
        bottom = face_locations[i][2]
        left = face_locations[i][3]

        start = (left, top)
        end = (right, bottom)

        color = (55,255,155)
        thickness = 1
        cv2.rectangle(img, start, end, color, thickness)

    # 显示识别结果
    cv2.imshow("newImage", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

face_reg(os.getcwd()+"/faces/tongliya.jpg")

