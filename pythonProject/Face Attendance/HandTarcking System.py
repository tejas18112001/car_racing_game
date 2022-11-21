
import cv2
import numpy as np
import HandTrackingModulee as htm
import time
import autopy

wcam, hcam = 1980, 600


cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
pTime = 0
while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(0)
# 11 th step Frame rate

cTime = Time.Time()
fps = 1/(cTime - pTime)
pTime = cTime
cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN,3,  (250, 0, 0),  3)



