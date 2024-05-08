import cv2

img = cv2.imread('/home/arun/Lum/OpenCV/gp2.jpg')

img1 = cv2.rectangle(img,pt1=(536,20),pt2=(929,148),color=(0,255,255),thickness=-1)
img1 = cv2.circle(img,center=(866,84),radius=65,color=(0,0,255),thickness=-1)
img1 = cv2.putText(img,text='luminar',org=(560,90),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,0),thickness=3)

cv2.imshow('image',img1)
cv2.waitKey()
cv2.destroyAllWindows()