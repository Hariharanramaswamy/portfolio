import cv2
import mediapipe as mp
import pyautogui
import threading
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

run_webcam_thread = True
mouse_down = False

def detect_and_click(frame):
    global mouse_down

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, _ = frame.shape
            x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            if index_finger_tip.y < 0.5:
                if not mouse_down:
                    pyautogui.mouseDown()
                    mouse_down = True
                    print("Left Click Hold")
            else:
                if mouse_down:
                    pyautogui.mouseUp()
                    mouse_down = False
                    print("Left Click Release")
    else:
        if mouse_down:
            pyautogui.mouseUp()
            mouse_down = False
            print("Left Click Release")

    return frame

def webcam_thread():
    global run_webcam_thread
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    6
    desired_fps = 60
    frame_duration = 1 / desired_fps
    
    while run_webcam_thread:
        start_time = time.time()
        
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break
        
        frame = detect_and_click(frame)
        
        cv2.imshow("Drogon Hills Control", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        elapsed_time = time.time() - start_time
        time_to_wait = frame_duration - elapsed_time
        if time_to_wait > 0:
            time.sleep(time_to_wait)
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    thread = threading.Thread(target=webcam_thread)
    thread.start()
    
    print("Webcam thread started. Press Ctrl+C to stop.")
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        run_webcam_thread = False
        thread.join()
        print("Webcam thread stopped.")
