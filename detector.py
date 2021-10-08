from os import closerange, write
import cv2
import mediapipe as mp
import csv
import pickle
from flaml import AutoML
import pandas as pd
import os
import glob

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

recording_name = ''
recording = False
detecting = False

def detect():

    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    # Webcam input:
    cap = cv2.VideoCapture(0)
    i = 0
    list = []

    with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:

        while cap.isOpened():

            # Get frame
            success, image = cap.read()

            # Check if frame is null
            if not success:
                print("Ignoring empty camera frame")
                # If loading a video, use 'break' instead of 'continue'.
                break

            # Flip the image horizontally for a later selfie-view display, and convert the BGR image to RGB
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

            # To improve performance, optionally mark the image as not writeable to pass by reference
            image.flags.writeable = False
            results = hands.process(image)

            # Revert
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Draw the hand annotations on the image and show it
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:

                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing_styles.get_default_hand_landmarks_style(), mp_drawing_styles.get_default_hand_connections_style())
                    image = cv2.resize(image, (1280, 720)) 
                    cv2.imshow('Detector', image)
                    
                    for data_point in hand_landmarks.landmark:
                        list.extend([data_point.x, data_point.y, data_point.z])

                    if detecting:
                        print(model.predict(pd.DataFrame([list])))

                    if recording:
                        with open('recordings/' + recording_name + '-' + str(i) + '.csv', "w", newline="") as f:
                            writer = csv.writer(f)
                            writer.writerow(list)                        
                        i += 1                        

                    list = []

            # Required
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()

def clear():
    files = glob.glob('recordings/*')
    for f in files:
        os.remove(f)
    print('cleared')
        
if detecting:
    detect()

