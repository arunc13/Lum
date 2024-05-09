import cv2

video = cv2.VideoCapture(0)

while True:
    success, frame = video.read()
    print(success) 

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame,1)
    (thresh,frame) = cv2.threshold(frame,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cv2.imshow('video reader', frame)
    if cv2.waitKey(1) & 0xFF==27:
        break
    
video.release()
cv2.destroyAllWindows()