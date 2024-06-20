import cv2
import mediapipe as mp
import pyautogui
import tkinter as tk
from tkinter import messagebox
import threading

# Initialize Face Mesh
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Get screen width and height
screen_w, screen_h = pyautogui.size()

# Flag to stop the eye control loop
stop_thread = False

# Default scaling factors
scaling_factor_x = 3.0
scaling_factor_y = 3.0

def start_eye_controlled_mouse():
    global stop_thread, scaling_factor_x, scaling_factor_y
    cam = cv2.VideoCapture(0)
    while not stop_thread:
        ret, frame = cam.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
                if id == 1:
                    # Adjust screen_x and screen_y with scaling factors
                    screen_x = screen_w * (landmark.x - 0.5) * scaling_factor_x + screen_w / 2
                    screen_y = screen_h * (landmark.y - 0.5) * scaling_factor_y + screen_h / 2
                    pyautogui.moveTo(screen_x, screen_y)
            left_eye_landmarks = [landmarks[145], landmarks[159]]
            for landmark in left_eye_landmarks:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)
            if (left_eye_landmarks[0].y - left_eye_landmarks[1].y) < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)
        cv2.imshow('Eye Controlled Mouse', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_thread = True
            break
    cam.release()
    cv2.destroyAllWindows()

def on_closing():
    global stop_thread
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        stop_thread = True
        root.destroy()

def check_stop_condition():
    global stop_thread
    if stop_thread:
        root.quit()
    root.after(100, check_stop_condition)

def start_thread():
    global stop_thread
    stop_thread = False
    thread = threading.Thread(target=start_eye_controlled_mouse)
    thread.start()

def update_scaling_factors_x(val):
    global scaling_factor_x
    scaling_factor_x = float(val)

def update_scaling_factors_y(val):
    global scaling_factor_y
    scaling_factor_y = float(val)

# Initialize Tkinter window
root = tk.Tk()
root.title("EYE MOUSE")
root.geometry("300x300")

# Start button
start_button = tk.Button(root, text="아이 마우스 시작하기", command=start_thread, width=30, height=2)
start_button.pack(pady=10)

# Scaling factor sliders
scaling_factor_x_slider = tk.Scale(root, from_=1.0, to=10.0, resolution=0.1, orient='horizontal', label='X축 민감도', command=update_scaling_factors_x)
scaling_factor_x_slider.set(scaling_factor_x)
scaling_factor_x_slider.pack(pady=10)

scaling_factor_y_slider = tk.Scale(root, from_=1.0, to=10.0, resolution=0.1, orient='horizontal', label='Y축 민감도', command=update_scaling_factors_y)
scaling_factor_y_slider.set(scaling_factor_y)
scaling_factor_y_slider.pack(pady=10)

# Handle window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Periodically check if the stop condition is met
root.after(100, check_stop_condition)

# Start Tkinter event loop
root.mainloop()
