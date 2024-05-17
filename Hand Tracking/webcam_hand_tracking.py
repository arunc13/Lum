import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils
hands = mp_hands.Hands()

video = cv2.VideoCapture('/home/arun/Lum/Hand Tracking/handsv1.mp4')

while True:
    success, frame = video.read()

    frame = cv2.resize(frame,(1280,720))

 #   frame = cv2.flip(frame,1)

    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    result = hands.process(frame)

    if result.multi_hand_landmarks:
        for hand_no, hand_land_marks in enumerate(result.multi_hand_landmarks):
            mp_drawings.draw_landmarks(image=frame, 
                                       landmark_list=hand_land_marks,
                                       connections=mp_hands.HAND_CONNECTIONS) 

    cv2.imshow('face detection', frame)
    if cv2.waitKey(1) & 0xFF==27:
        break

video.release()
cv2.destroyAllWindows()