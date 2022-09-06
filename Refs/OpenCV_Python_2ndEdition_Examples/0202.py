# 0202.py
import cv2
import numpy as np

imageFile = './data/lena.jpg'

img = cv2.imread(imageFile) 
cv2.imshow('lena',img)
cv2.imwrite('./data/Lena.bmp', img)
cv2.imwrite('./data/Lena.png', img)
cv2.imwrite('./data/Lena2.png',img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 5])


imageFile = './data/lena2.jpg'
img  = cv2.imread(imageFile)    # cv2.IMREAD_COLOR

##encode_img = np.fromfile(imageFile, np.uint8)
##img = cv2.imdecode(encode_img, cv2.IMREAD_UNCHANGED)

cv2.imshow('Lena 2nd',img)


cv2.waitKey()
cv2.destroyAllWindows()

