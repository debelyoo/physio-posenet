import numpy as np
import cv2
import time

cap = cv2.VideoCapture(2)

factor = 2.5

fgbg = cv2.createBackgroundSubtractorMOG2()

for x in range(0,120):
    ret, frame = cap.read()
    if ret == 0:
        break
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


print("Stand still for a little bit")
threshold = 0
for x in range(0,30):
    ret, frame = cap.read()
    if ret == 0:
        break
    fgmask = fgbg.apply(frame)
    threshold = threshold + fgmask.sum()
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
threshold = threshold / 30
print('El threshold es ')
print(threshold)

first = True
while(1):
    ret, frame = cap.read()
    if ret == 0:
        break
    fgmask = fgbg.apply(frame)
    currentsum = fgmask.sum()
    #print(currentsum)
    if(currentsum < factor*threshold):
        show = "ESTA QUIET"
    else:
        show = "ESTA EN MOVIMENT"
    cv2.putText(frame, show, (50, 50), cv2.FONT_HERSHEY_COMPLEX, .8, (255, 50, 0), 2, lineType=cv2.LINE_AA)
    cv2.imshow('frame',frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
