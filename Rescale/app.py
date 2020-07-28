import numpy as np
import cv2

cap=cv2.VideoCapture(0)

def resolution(width,height):
    cap.set(3,width)
    cap.set(4,height)

resolution(640,480)
while True:
    ret,frame=cap.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()