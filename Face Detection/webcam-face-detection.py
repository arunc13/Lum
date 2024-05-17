import cv2

video = cv2.VideoCapture('/home/arun/Lum/Face Detection/wav1.mp4')
# video = cv2.VideoCapture(0)

while True:
    success, frame = video.read()

    face_cascade = cv2.CascadeClassifier('/home/arun/Lum/Face Detection/haarcascade_frontalface_default.xml')

    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame_gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0), thickness=2)

    cv2.imshow('face detection', frame)
    if cv2.waitKey(1) & 0xFF==27:
        break

video.release()
cv2.destroyAllWindows()