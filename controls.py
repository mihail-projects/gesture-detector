import tkinter
from tkinter.constants import DISABLED, NORMAL
import recorder
import threading
import os
import sys


def controls():

    window = tkinter.Tk()
    window.title('Gestures')
    window.geometry('140x50')

    def record():
        recorder.recording = True
        record_btn['state'] = DISABLED
        detect_btn['state'] = DISABLED
        stop_btn['state'] = NORMAL

    def stop():
        os._exit(1)

    def detect():
        recorder.detecting = True
        record_btn['state'] = DISABLED
        detect_btn['state'] = DISABLED
        stop_btn['state'] = NORMAL

    record_btn_img = tkinter.PhotoImage(file='UI/record.png')
    record_btn_lbl = tkinter.Label(image=record_btn_img)
    record_btn = tkinter.Button(window, image=record_btn_img, command=record, borderwidth=0)
    record_btn.place(x=10, y=10)

    stop_btn_img = tkinter.PhotoImage(file='UI/stop.png')
    stop_btn_lbl = tkinter.Label(image=stop_btn_img)
    stop_btn = tkinter.Button(window, image=stop_btn_img, command=stop, borderwidth=0)
    stop_btn['state'] = DISABLED
    stop_btn.place(x=55, y=12)

    detect_btn_img = tkinter.PhotoImage(file='UI/detect.png')
    detect_btn_lbl = tkinter.Label(image=detect_btn_img)
    detect_btn = tkinter.Button(window, image=detect_btn_img, command=detect, borderwidth=0)
    detect_btn['state'] = NORMAL
    detect_btn.place(x=100, y=12)

    if len(sys.argv) == 1:
        record_btn['state'] = DISABLED

    window.mainloop()

if(len(sys.argv) > 1):
    recorder.gesture_name = sys.argv[1]

controlsT = threading.Thread(target=controls)
detectorT = threading.Thread(target=recorder.detect)

controlsT.start()
detectorT.start()
controlsT.join()
detectorT.join()
