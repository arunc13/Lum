import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('/home/arun/Lum/OCR/T1.png')
# img = cv2.imread('/home/arun/Lum/OCR/T2.jpeg')
# img = cv2.imread('/home/arun/Lum/OCR/T3.jpg')
# img = cv2.imread('/home/arun/Lum/OCR/T4.jpg')

text = pytesseract.image_to_string(img)
data = pytesseract.image_to_data(img, output_type=Output.DICT)

print(text)
print(data.keys())
print(data['text'])
print(data['conf'])

n_boxes = len(data['text'])
print(n_boxes)



cv2.imshow('text',img)
cv2.waitKey()
cv2.destroyAllWindows()