import cv2

img = cv2.imread('/home/arun/Lum/Face Detection/gp2.jpg')

eye_cascade = cv2.CascadeClassifier('/home/arun/Lum/Face Detection/haarcascade_eye.xml')

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

eyes = eye_cascade.detectMultiScale(gray_img)

print(eyes)

for (x,y,w,h) in eyes:
    cv2.rectangle(img, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0), thickness=2)

cv2.imshow('gp2.jpg',img)
cv2.waitKey()
cv2.destroyAllWindows()