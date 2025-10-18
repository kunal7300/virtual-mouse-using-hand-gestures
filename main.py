import cv2
import mediapipe as mp
import pyautogui
import math

# Initialize
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

click_down = False
right_click_down = False
action_text = ""   # text to display on screen

def get_distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # mirror view
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    action_text = ""  # reset text each frame

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Landmarks for fingers
            x_index, y_index = hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y
            x_middle, y_middle = hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y
            x_ring, y_ring = hand_landmarks.landmark[16].x, hand_landmarks.landmark[16].y
            x_pinky, y_pinky = hand_landmarks.landmark[20].x, hand_landmarks.landmark[20].y

            # Convert to screen coordinates
            x_screen = int(x_index * screen_width)
            y_screen = int(y_index * screen_height)
            pyautogui.moveTo(x_screen, y_screen)

            # Finger extended check (tip higher than joint below it)
            index_up = y_index < hand_landmarks.landmark[6].y
            middle_up = y_middle < hand_landmarks.landmark[10].y
            ring_up = y_ring < hand_landmarks.landmark[14].y
            pinky_up = y_pinky < hand_landmarks.landmark[18].y

            fingers_up = [index_up, middle_up, ring_up, pinky_up]
            total_fingers = sum(fingers_up)

            # Right Click → one finger (only index up)
            if total_fingers == 1 and index_up:
                if not right_click_down:
                    pyautogui.rightClick()
                    right_click_down = True
                    action_text = "Right Click"
            else:
                right_click_down = False

            # Left Click → two fingers (index + middle up)
            if total_fingers == 2 and index_up and middle_up:
                if not click_down:
                    pyautogui.click()
                    click_down = True
                    action_text = "Left Click"
            else:
                click_down = False

            # Exit → Fist (no fingers up)
            if total_fingers == 0:
                action_text = "Exit (Fist)"
                cv2.putText(frame, action_text, (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                cv2.imshow("Hand Mouse Control", frame)
                cap.release()
                cv2.destroyAllWindows()
                quit()

    # Draw action text on screen
    if action_text:
        cv2.putText(frame, action_text, (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Hand Mouse Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
quit()
