# import numpy as np
import cv2

# multiple cascades:
# https://github.com/Itseez/opencv/tree/master/data/haarcascades

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
cap = cv2.VideoCapture(0)
# image = cv2.imread('Images/bateau.bmp', 255)
# cv2.imshow('image', image)
# cv2.waitKey(0)
while 1:
    nombre_face = 0
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = img[y : y + h, x : x + w]
        nombre_face += 1

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow("Face", img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
    elif nombre_face == 1:
        print("Il y a une personne")
    elif nombre_face > 1:
        print("Il y à " + str(nombre_face) + " personnes")

cap.release()
cv2.destroyAllWindows()
