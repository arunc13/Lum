import mediapipe as mp
import cv2

img = cv2.imread('/home/arun/Lum/Hand Tracking/hand.jpeg')

rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

converted = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2)

result = hands.process(rgb_img)

print(result.multi_handedness)

print(result.multi_hand_landmarks)

cv2.imshow('hand tracking',img)
cv2.waitKey()
cv2.destroyAllWindows()