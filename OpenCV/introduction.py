import cv2

img = cv2.imread('/home/arun/Lum/OpenCV/gp1.jpg')
img1 = cv2.imread('/home/arun/Lum/OpenCV/gp2.jpg')
# print(img)

print(img.shape)  # (h,w,c) c -> rgb/bw
resized_image = cv2.resize(img1,(640,480))


gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

(thresh,bw_img) = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(thresh)

# rectangle
img1_rec = cv2.rectangle(img1,pt1=(272,220),pt2=(426,436),color=(0,0,255),thickness=2)

# circle
img1_circle = cv2.circle(img1,center=(778,364),radius=120,color=(0,255,0),thickness=2)

# text
img1_text = cv2.putText(img1,text='luminar',org=(668,45),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=2,color=(255,255,0),thickness=3)

cv2.imwrite('gp1_gray.jpg',gray_img)
cv2.imwrite('gp1_bw.jpg',bw_img)

cv2.imshow('image',bw_img)
cv2.imshow('image2',resized_image)
cv2.imshow('image3',img1_rec)
cv2.waitKey()
cv2.destroyAllWindows()