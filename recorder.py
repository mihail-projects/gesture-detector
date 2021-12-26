import cv2
import mediapipe
import csv
import pickle
import pandas
import os
import sys

mp_drawing = mediapipe.solutions.drawing_utils
mp_drawing_styles = mediapipe.solutions.drawing_styles
mp_hands = mediapipe.solutions.hands

recording = False
detecting = False
gesture_name = ''

fields = ['label', 'x0', 'y0', 'z0', 'x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3', 'x4', 'y4', 'z4', 
                   'x5', 'y5', 'z5', 'x6', 'y6', 'z6', 'x7', 'y7', 'z7', 'x8', 'y8', 'z8', 'x9', 'y9', 'z9', 
                   'x10', 'y10', 'z10', 'x11', 'y11', 'z11', 'x12', 'y12', 'z12', 'x13', 'y13', 'z13', 'x14', 
                   'y14', 'z14', 'x15', 'y15', 'z15', 'x16', 'y16', 'z16', 'x17', 'y17', 'z17', 'x18', 'y18', 
                   'z18', 'x19', 'y19', 'z19', 'x20', 'y20', 'z20']

if os.path.exists("ML/model.pkl"):
    with open("ML/model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

f = open('ML/data.csv', "a", newline="")
writer = csv.DictWriter(f, fieldnames=fields)
writer.writeheader()                            

if os.path.getsize('ML/data.csv') > 0:
    samples = len(pandas.read_csv('ML/data.csv'))
else:
    samples = 0

def detect():

    # Webcam input:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

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

                    if recording:
                        
                        dict = {}
                        dict['label'] = gesture_name
                        for i in range(21):
                            dict['x'+str(i)] = f'{results.multi_hand_landmarks[0].landmark[i].x:.7f}'
                            dict['y'+str(i)] = f'{results.multi_hand_landmarks[0].landmark[i].y:.7f}'
                            dict['z'+str(i)] = f'{results.multi_hand_landmarks[0].landmark[i].z:.7f}'                      
                        writer.writerow(dict)

                        if os.path.getsize('ML/data.csv') > 0:
                            sys.stdout.write("\rTotal: " + str(len(pandas.read_csv('ML/data.csv'))) + " - Current: " + str(abs(samples - len(pandas.read_csv('ML/data.csv')))))
                            sys.stdout.flush()  

                    if detecting:

                        list = []

                        for i in range(21):
                            list.append(f'{results.multi_hand_landmarks[0].landmark[i].x:.7f}')
                            list.append(f'{results.multi_hand_landmarks[0].landmark[i].y:.7f}')
                            list.append(f'{results.multi_hand_landmarks[0].landmark[i].z:.7f}')

                        if 'label' in fields: fields.remove('label')
                        df = pandas.DataFrame([list], columns=fields)
                        print(model.predict(df))                    

            #image = cv2.resize(image, (1280, 720))
            cv2.imshow('Detector', image)

            # Required
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()
