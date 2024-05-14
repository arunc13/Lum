import cv2
import pytesseract
from pytesseract import Output
import re

invoice = cv2.imread('/home/arun/Lum/OCR/Invoice.jpeg')

text = pytesseract.image_to_string(invoice)
data = pytesseract.image_to_data(invoice, output_type=Output.DICT)

print(text)
print(data.keys())
print(data['text'])
print(data['conf'])

n_boxes = len(data['text'])
print('No of text:', n_boxes)

date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
mail_pattern = '^[a-z0-9](\.?[a-z0-9]){5,}@example\.net$'

for i in range(n_boxes):
    if data['conf'][i] > 60:
        if re.match(date_pattern, data['text'][i]) or re.match(mail_pattern, data['text'][i]):
            x,y,w,h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            cv2.rectangle(invoice, (x,y), (x+w,y+h), color=(0,255,0), thickness=5)

cv2.imshow('text',invoice)
cv2.waitKey()
cv2.destroyAllWindows()