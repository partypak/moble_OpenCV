# 0207.py
import cv2
import numpy as np

##cap = cv2.VideoCapture(0)  # 0번 카메라
cap = cv2.VideoCapture('./data/vtest.avi')
##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
##cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)
imageFile = './data/lena.jpg'

lena = cv2.imread(imageFile) 
ratio1 = 0.6
ratio2 = 0.4

while True:   
    retval, frame = cap.read()
    if not retval:
        break
    
    lena =cv2.resize(lena,(640,480))
    frame =cv2.resize(frame,(640,480))
    text = 'Hello'
    org = (100,470)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,text, org, font, 1, (255,0,0), 2)
    add=cv2.add(frame,lena)
    cv2.imshow('frame',add)
    
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
