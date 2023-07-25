#!/usr/bin/python

import cv2

print(cv2.__version__)

cap = cv2.VideoCapture("/dev/video0",cv2.CAP_V4L)

_, image = cap.read()
print(image)
cv2.imwrite('hello.jpg',image)
