from PIL import Image
import pytesseract
 
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
 
str = pytesseract.image_to_string(Image.open('.\data\sample2.jpg'), lang='kor')
 
print(str)
