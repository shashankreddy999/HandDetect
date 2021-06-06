import cv2
import time
import numpy as np
import HandTrackingModule as htm
import pyautogui
import math


################################
wCam, hCam = 1920, 1080
################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    img=cv2.flip(img,1)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        x3, y3 = lmList[0][1], lmList[0][2]
        pyautogui.moveTo(x3,y3)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break