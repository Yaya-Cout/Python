# import the necessary packages
from __future__ import print_function

# import numpy as np
import cv2

# load the image
image = cv2.imread("/home/neo/Images/Foret.jpg")
cap = cv2.VideoCapture(0)
ret, image = cap.read()


def addWaterMark(text, opacity, BGRColor):
    ret, image = cap.read()
    opacity = opacity / 100
    overlay = image.copy()
    output = image.copy()
    cv2.putText(
        overlay,
        text,
        (0, int(2 * (image.shape[1]) / 3)),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        BGRColor,
        2,
    )
    # apply the overlay
    cv2.addWeighted(overlay, opacity, output, 1 - opacity, 0, output)
    # show the output image
    cv2.imshow("Output", output)
    # cv2.waitKey(0)

    del opacity, overlay, output


if __name__ == "__main__":
    # put the text , Opacity, BGR Color
    while 1:
        addWaterMark("Life2Coding", 50, (255, 0, 255))
