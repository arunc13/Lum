import cv2
import HandTrackingModule as ht
import numpy as np

detector = ht.handDetector()

cap = cv2.VideoCapture('/home/arun/Lum/Virtual Painter/wav1.mp4')
cap = cv2.VideoCapture(0)

draw_color = (255,255,255)
img_canvas = np.zeros((720,1280,3), np.uint8)

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
    # print(lmlist)
    if len(lmlist) != 0:
        # tip of index and middle fingers
        x1,y1 = lmlist[8][1:]
        x2,y2 = lmlist[12][1:]
        # Check which finger is up
        fingers = detector.fingersUp()
        # print(fingers)
        # Selection mode - 2 finger up condition (index finger & middle finger)
        if fingers[1] and fingers[2]:
            # print('selection mode')
            xp,yp = 0,0  # Previous point (Coordinates)
            if y1<=100:
                if 20<x1<210:
                    print('red')
                    draw_color = (0,0,255)
                elif 230<x1<450:
                    print('green')
                    draw_color = (0,255,0)
                elif 470<x1<680:
                    print('blue')
                    draw_color = (255,0,0)
                elif 700<x1<920:
                    print('yellow')
                    draw_color = (0,255,255)
                elif 940<x1<1260:
                    print('eraser')
                    draw_color = (0,0,0)
            cv2.rectangle(frame,(x1,y1),(x2,y2),color=draw_color,thickness=-1)
        # Drawing mode - 1 finger up condition (index finger)
        if fingers[1] and not fingers[2]:
            print('drawing mode')
            cv2.circle(frame,(x1,y1),15,draw_color,thickness=-1)
            #x1,y1 = # Current point (Coordinates)
            if xp==0 and yp==0:
                xp=x1
                yp=y1
            if draw_color == (0,0,0):
                cv2.line(frame,(xp,yp),(x1,y1),color=draw_color,thickness=30)
                cv2.line(img_canvas,(xp,yp),(x1,y1),color=draw_color,thickness=30)
            else:
                cv2.line(frame,(xp,yp),(x1,y1),color=draw_color,thickness=5)
                cv2.line(img_canvas,(xp,yp),(x1,y1),color=draw_color,thickness=5)
            xp,yp = x1,y1
            
    img_gray = cv2.cvtColor(img_canvas,cv2.COLOR_BGR2GRAY)
    ret,img_inv = cv2.threshold(img_gray,20,255,cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv,cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame,img_inv)
    frame = cv2.bitwise_or(frame,img_canvas)

    frame = cv2.addWeighted(frame,1,img_canvas,.5,0)
    
    cv2.imshow('irtual painter', frame)
    cv2.imshow('image canvas',img_canvas)
    if cv2.waitKey(1) & 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()