import face_recognition
import os
import cv2

tong_image = face_recognition.load_image_file(os.getcwd()+"/faces/3445.jpg")
tong_marks = face_recognition.face_landmarks(tong_image)
num = 0
tong_image = cv2.imread(os.getcwd()+"/faces/fff.jpg")
for a in range(len(tong_marks)):
    for key in tong_marks[a]:
        pt_color = (0, 0, 255)
        for i in range(len(tong_marks[a][key])):
            cv2.circle(tong_image, tong_marks[a][key][i], 0, pt_color, 4)
            #cv2.putText(tong_image, str(num), (tong_marks[key][i][0]-2, tong_marks[key][i][1]+2), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0, 255, 0), 1)
            num = num + 1
print(num)
cv2.imshow("out", tong_image)
cv2.waitKey(0)