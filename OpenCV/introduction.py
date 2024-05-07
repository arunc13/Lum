import cv2

img = cv2.imread('/home/arun/Lum/OpenCV/gp1.jpg')
print(img)

cv2.imshow('image',img)
cv2.waitKey(50000)
cv2.destroyAllWindows()