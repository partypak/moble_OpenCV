# 0407.py
import cv2
 
src = cv2.imread('./data/lena.jpg')
roi = cv2.selectROI(src)
print('roi =', roi)

if roi != (0, 0, 0, 0):
    img = src[roi[1]:roi[1]+roi[3],
               roi[0]:roi[0]+roi[2]]
    cv2.imwrite('./data/cok.jpg', img)
    cv2.imshow('Img', img)
    cv2.waitKey()
    
cv2.destroyAllWindows()
