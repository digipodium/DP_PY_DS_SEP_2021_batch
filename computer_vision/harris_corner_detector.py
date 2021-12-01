import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    dst = cv.cornerHarris(gray,2,3,0.04)
    dst = cv.dilate(dst,None)
    frame[dst>0.01*dst.max()]=[255,0,255]
    cv.imshow('dst',frame)
    if cv.waitKey(1) == 27: # esc to quit
        break
cap.release()
cv.destroyAllWindows()
