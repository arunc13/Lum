import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_drawings = mp.solutions.drawing_utils
pose = mp_pose.Pose()

video = cv2.VideoCapture('/home/arun/Lum/Hand Tracking/wav1.mp4')
#video = cv2.VideoCapture(0)

while True:
    x,frame = video.read()
 #   frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(1280,720))

    results = pose.process(frame)

    print(results.pose_landmarks)

    if results.pose_landmarks:
        mp_drawings.draw_landmarks(image=frame,
                                   landmark_list=results.pose_landmarks,
                                   connections=mp_pose.POSE_CONNECTIONS)

    cv2.imshow('human body tracking',frame)

    if cv2.waitKey(1) & 0xFF==27:
        break

video.release()
cv2.destroyAllWindows()