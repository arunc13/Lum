import cv2
import HandTrackingModule as ht

detector = ht.handDetector()

cap = cv2.VideoCapture('/home/arun/Lum/Virtual Painter/wav1.mp4')
cap = cv2.VideoCapture(0)

while 1:
    success, frame = cap.read()

    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(1280,720))

    cv2.rectangle(frame,pt1=(10,10),pt2=(210,100),color=(0,0,255),thickness=-1)
    cv2.rectangle(frame,pt1=(230,10),pt2=(450,100),color=(0,255,0),thickness=-1)
    cv2.rectangle(frame,pt1=(470,10),pt2=(680,100),color=(255,0,0),thickness=-1)
    cv2.rectangle(frame,pt1=(700,10),pt2=(920,100),color=(0,255,255),thickness=-1)
    cv2.rectangle(frame,pt1=(940,10),pt2=(1260,100),color=(255,255,255),thickness=-1)
    cv2.putText(frame,text='ERASER',org=(1035,65),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,0),thickness=3)

# Find hands and landmarks

    frame = detector.findHands(frame)
    lmlist = detector.findPosition(frame, draw=False)
    print(lmlist)

# Check which finger is up

# Selection mode - 2 finger up condition

# Drawing mode - 1 finger up condition

    cv2.imshow('irtual painter', frame)
    if cv2.waitKey(1) & 0xFF==27:
        break



cap.realease()
cv2.destroyAllWindows()