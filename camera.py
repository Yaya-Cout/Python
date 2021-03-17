#!/bin/python3
import cv2

c = cv2.VideoCapture(0)

while 1:
    _, f = c.read()
    cv2.imshow("Camera", f)
    k = cv2.waitKey(5)
    if k == 27:
        # Esc key to stop, or 27 depending your keyboard
        # Touche ESC appuyee. le code peut dependre du clavier. Normalement 27
        break
    elif k == -1:
        continue
    # uncomment to know the code of of the key pressed
    # Decommenter pour connaitre le code de la touche pressee
    else:
        print(k)

cv2.destroyAllWindows()
