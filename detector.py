import cv2
import mediapipe as mp
import csv
import pickle
import pandas as pd
import os
import sys
import numpy as np
import keyboard

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

recording = False
detecting = False
gesture_name = ''


def detect():

    fieldnames = ['label',
                  'feature1x', 'feature1y', 'feature1z',
                  'feature2x', 'feature2y', 'feature2z',
                  'feature3x', 'feature3y', 'feature3z',
                  'feature4x', 'feature4y', 'feature4z',
                  'feature5x', 'feature5y', 'feature5z',
                  'feature6x', 'feature6y', 'feature6z',
                  'feature7x', 'feature7y', 'feature7z',
                  'feature8x', 'feature8y', 'feature8z',
                  'feature9x', 'feature9y', 'feature9z',
                  'feature10x', 'feature10y', 'feature10z',
                  'feature11x', 'feature11y', 'feature11z',
                  'feature12x', 'feature12y', 'feature12z',
                  'feature13x', 'feature13y', 'feature13z',
                  'feature14x', 'feature14y', 'feature14z',
                  'feature15x', 'feature15y', 'feature15z',
                  'feature16x', 'feature16y', 'feature16z',
                  'feature17x', 'feature17y', 'feature17z',
                  'feature18x', 'feature18y', 'feature18z',
                  'feature19x', 'feature19y', 'feature19z',
                  'feature20x', 'feature20y', 'feature20z',
                  'feature21x', 'feature21y', 'feature21z']

    with open("ML/model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    # Webcam input:
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:

        with open('ML/data.csv', "a", newline="") as f:

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            fieldnames.remove('label')

            if os.stat('ML/data.csv').st_size == 0:
                writer.writeheader()

            while cap.isOpened():

                if keyboard.is_pressed('q'):
                    os._exit(1)

                # Get frame
                success, image = cap.read()

                # Check if frame is null
                if not success:
                    print("Ignoring empty camera frame")
                    # If loading a video, use 'break' instead of 'continue'.
                    continue

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
                        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing_styles.get_default_hand_landmarks_style(
                        ), mp_drawing_styles.get_default_hand_connections_style())
                        image = cv2.resize(image, (1280, 720))
                        cv2.imshow('Detector', image)

                    if recording:

                        if os.stat('ML/data.csv').st_size > 0:
                            sys.stdout.write("\rSamples: %i" % len(
                                pd.read_csv('ML/data.csv')))
                            sys.stdout.flush()

                        writer.writerow({'label': gesture_name,

                                         'feature1x': f'{results.multi_hand_landmarks[0].landmark[0].x:.20f}',
                                         'feature1y': f'{results.multi_hand_landmarks[0].landmark[0].y:.20f}',
                                         'feature1z': f'{results.multi_hand_landmarks[0].landmark[0].z:.20f}',

                                         'feature2x': f'{results.multi_hand_landmarks[0].landmark[1].x:.20f}',
                                         'feature2y': f'{results.multi_hand_landmarks[0].landmark[1].y:.20f}',
                                         'feature2z': f'{results.multi_hand_landmarks[0].landmark[1].z:.20f}',

                                         'feature3x': f'{results.multi_hand_landmarks[0].landmark[2].x:.20f}',
                                         'feature3y': f'{results.multi_hand_landmarks[0].landmark[2].y:.20f}',
                                         'feature3z': f'{results.multi_hand_landmarks[0].landmark[2].z:.20f}',

                                         'feature4x': f'{results.multi_hand_landmarks[0].landmark[3].x:.20f}',
                                         'feature4y': f'{results.multi_hand_landmarks[0].landmark[3].y:.20f}',
                                         'feature4z': f'{results.multi_hand_landmarks[0].landmark[3].z:.20f}',

                                         'feature5x': f'{results.multi_hand_landmarks[0].landmark[4].x:.20f}',
                                         'feature5y': f'{results.multi_hand_landmarks[0].landmark[4].y:.20f}',
                                         'feature5z': f'{results.multi_hand_landmarks[0].landmark[4].z:.20f}',

                                         'feature6x': f'{results.multi_hand_landmarks[0].landmark[5].x:.20f}',
                                         'feature6y': f'{results.multi_hand_landmarks[0].landmark[5].y:.20f}',
                                         'feature6z': f'{results.multi_hand_landmarks[0].landmark[5].z:.20f}',

                                         'feature7x': f'{results.multi_hand_landmarks[0].landmark[6].x:.20f}',
                                         'feature7y': f'{results.multi_hand_landmarks[0].landmark[6].y:.20f}',
                                         'feature7z': f'{results.multi_hand_landmarks[0].landmark[6].z:.20f}',

                                         'feature8x': f'{results.multi_hand_landmarks[0].landmark[7].x:.20f}',
                                         'feature8y': f'{results.multi_hand_landmarks[0].landmark[7].y:.20f}',
                                         'feature8z': f'{results.multi_hand_landmarks[0].landmark[7].z:.20f}',

                                         'feature9x': f'{results.multi_hand_landmarks[0].landmark[8].x:.20f}',
                                         'feature9y': f'{results.multi_hand_landmarks[0].landmark[8].y:.20f}',
                                         'feature9z': f'{results.multi_hand_landmarks[0].landmark[8].z:.20f}',

                                         'feature10x': f'{results.multi_hand_landmarks[0].landmark[9].x:.20f}',
                                         'feature10y': f'{results.multi_hand_landmarks[0].landmark[9].y:.20f}',
                                         'feature10z': f'{results.multi_hand_landmarks[0].landmark[9].z:.20f}',

                                         'feature11x': f'{results.multi_hand_landmarks[0].landmark[10].x:.20f}',
                                         'feature11y': f'{results.multi_hand_landmarks[0].landmark[10].y:.20f}',
                                         'feature11z': f'{results.multi_hand_landmarks[0].landmark[10].z:.20f}',

                                         'feature12x': f'{results.multi_hand_landmarks[0].landmark[11].x:.20f}',
                                         'feature12y': f'{results.multi_hand_landmarks[0].landmark[11].y:.20f}',
                                         'feature12z': f'{results.multi_hand_landmarks[0].landmark[11].z:.20f}',

                                         'feature13x': f'{results.multi_hand_landmarks[0].landmark[12].x:.20f}',
                                         'feature13y': f'{results.multi_hand_landmarks[0].landmark[12].y:.20f}',
                                         'feature13z': f'{results.multi_hand_landmarks[0].landmark[12].z:.20f}',

                                         'feature14x': f'{results.multi_hand_landmarks[0].landmark[13].x:.20f}',
                                         'feature14y': f'{results.multi_hand_landmarks[0].landmark[13].y:.20f}',
                                         'feature14z': f'{results.multi_hand_landmarks[0].landmark[13].z:.20f}',

                                         'feature15x': f'{results.multi_hand_landmarks[0].landmark[14].x:.20f}',
                                         'feature15y': f'{results.multi_hand_landmarks[0].landmark[14].y:.20f}',
                                         'feature15z': f'{results.multi_hand_landmarks[0].landmark[14].z:.20f}',

                                         'feature16x': f'{results.multi_hand_landmarks[0].landmark[15].x:.20f}',
                                         'feature16y': f'{results.multi_hand_landmarks[0].landmark[15].y:.20f}',
                                         'feature16z': f'{results.multi_hand_landmarks[0].landmark[15].z:.20f}',

                                         'feature17x': f'{results.multi_hand_landmarks[0].landmark[16].x:.20f}',
                                         'feature17y': f'{results.multi_hand_landmarks[0].landmark[16].y:.20f}',
                                         'feature17z': f'{results.multi_hand_landmarks[0].landmark[16].z:.20f}',

                                         'feature18x': f'{results.multi_hand_landmarks[0].landmark[17].x:.20f}',
                                         'feature18y': f'{results.multi_hand_landmarks[0].landmark[17].y:.20f}',
                                         'feature18z': f'{results.multi_hand_landmarks[0].landmark[17].z:.20f}',

                                         'feature19x': f'{results.multi_hand_landmarks[0].landmark[18].x:.20f}',
                                         'feature19y': f'{results.multi_hand_landmarks[0].landmark[18].y:.20f}',
                                         'feature19z': f'{results.multi_hand_landmarks[0].landmark[18].z:.20f}',

                                         'feature20x': f'{results.multi_hand_landmarks[0].landmark[19].x:.20f}',
                                         'feature20y': f'{results.multi_hand_landmarks[0].landmark[19].y:.20f}',
                                         'feature20z': f'{results.multi_hand_landmarks[0].landmark[19].z:.20f}',

                                         'feature21x': f'{results.multi_hand_landmarks[0].landmark[20].x:.20f}',
                                         'feature21y': f'{results.multi_hand_landmarks[0].landmark[20].y:.20f}',
                                         'feature21z': f'{results.multi_hand_landmarks[0].landmark[20].z:.20f}'})

                    if detecting:

                        list = [f'{results.multi_hand_landmarks[0].landmark[0].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[0].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[0].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[1].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[1].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[1].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[2].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[2].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[2].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[3].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[3].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[3].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[4].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[4].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[4].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[5].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[5].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[5].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[6].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[6].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[6].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[7].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[7].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[7].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[8].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[8].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[8].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[9].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[9].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[9].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[10].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[10].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[10].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[11].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[11].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[11].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[12].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[12].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[12].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[13].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[13].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[13].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[14].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[14].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[14].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[15].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[15].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[15].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[16].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[16].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[16].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[17].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[17].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[17].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[18].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[18].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[18].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[19].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[19].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[19].z:.20f}',

                                f'{results.multi_hand_landmarks[0].landmark[20].x:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[20].y:.20f}',
                                f'{results.multi_hand_landmarks[0].landmark[20].z:.20f}']

                        df = pd.DataFrame([list], columns=fieldnames)
                        print(model.predict(df))

                # Required
                if cv2.waitKey(5) & 0xFF == 27:
                    break

    cap.release()
