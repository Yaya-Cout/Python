# import cv2
# # Readingour Image1
# # my_firstpic = cv2.imread(
# # 'C:/Users/TP/Pictures/west bengal/bishnupur/mqdefaultILPT6GSR.jpg', 1)

# my_first = cv2.imread(
#     '/home/neo/Téléchargements/Photo_camille.jpg', 1)
# cv2.imshow('image', my_first)
# # Readingour Image2
# cap = cv2.VideoCapture(0)
# ret, my_sec = cap.read()

# img = cv2.add(my_first, my_sec)
# cv2.waitKey(0)
# cv2.distroyAllWindows()
import cv2
import numpy as np

img = cv2.imread("pyimg.jpg")
contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)

cv2.imshow("Original Image", img)

cv2.imshow("Contrast Image", contrast_img)

cv2.waitKey(0)
