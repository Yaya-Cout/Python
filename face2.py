# import cv2
# # img1 = cv2.imread('D:/downloads/pasta_screen.jpg')
# cap = cv2.VideoCapture(0)
# ret, img1 = cap.read()
# del ret, cap
# img2 = cv2.imread('/home/neo/Téléchargements/ubuntu-icon.jpg')
# rows, cols, channels = img2.shape
# roi = img1[0:rows, 0:cols]
# img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY_INV)
# mask_inv = cv2.bitwise_not(mask)
# img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
# img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
# out_img = cv2.add(img1_bg, img2_fg)
# img1[0:rows, 0:cols] = out_img
# cv2.imshow('Face', out_img)
# cv2.waitKey(0)

from numpy import *
import cv2
cap = cv2.VideoCapture(0)
ret, src1 = cap.read()
# del ret, cap
src2 = cv2.imread(
    '/home/neo/Images/Foret.jpg', cv2.IMREAD_COLOR)
print(src1.shape)
print(src2.shape)
# dst = cv2.addWeighted(src1, 1, src2, 1, 0.0)
# img = cv2.addWeighted(src1, 0.3, src2, 0.7, 0)
# add or blend the images

scale_percent = 0.1  # percent of original size
width = int(src2.shape[1] * scale_percent / 100)
height = int(src2.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
# src2 = cv2.resize(src2, dim, interpolation=cv2.INTER_AREA)

# resize image
width = int(src1.shape[0]/2)
height = int(src1.shape[1]/2)
dim = (width, height)

src2 = cv2.resize(src2, dim, interpolation=cv2.INTER_AREA)


def overlay_image(im1, im2, x_offset, y_offset):
    '''Mutates im1, placing im2 over it at a given offset.'''
    im1[y_offset: y_offset + im2.shape[0],
        x_offset: x_offset + im2.shape[1]] = im2
    return im2


img = overlay_image(src1, src2, 10, 10)
# img = src1 + src2
# img = cv2.add(src1, src2)
# cv2.imshow('image', src1)
# img = cv2.add(src1, src2)

cv2.imshow('Face', img)
# cv2.imshow('image', src2)
cv2.waitKey(0)
