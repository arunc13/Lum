import cv2

img = cv2.imread('/home/arun/Lum/OpenCV/gp1.jpg')
img1 = cv2.imread('/home/arun/Lum/OpenCV/gp2.jpg')
# print(img)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

(thresh,bw_img) = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(thresh)

cv2.imwrite('gp1_gray.jpg',gray_img)
cv2.imwrite('gp1_bw.jpg',bw_img)

cv2.imshow('image',bw_img)
cv2.imshow('image2',img1)
cv2.waitKey()
cv2.destroyAllWindows()