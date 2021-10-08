import tkinter
from tkinter.constants import DISABLED, NORMAL
import detector
import threading
import os

def controls():

    window = tkinter.Tk()
    window.title('Recorder')
    window.geometry('250x50')

    def record():
        if recording_name.get('1.0', 'end-1c') != '':
            os.mkdir('recordings/' + recording_name.get('1.0', 'end-1c'))
            detector.recording_name = recording_name.get('1.0', 'end-1c')
            detector.recording = True
            record_btn['state'] = DISABLED
            stop_btn['state'] = NORMAL
            recording_name['state'] = DISABLED

    def stop():
        detector.recording_name = ''
        detector.recording = False
        record_btn['state'] = NORMAL
        stop_btn['state'] = DISABLED
        recording_name['state'] = NORMAL

    record_btn_img = tkinter.PhotoImage(file='record.png')
    record_btn_lbl = tkinter.Label(image=record_btn_img)
    record_btn = tkinter.Button(window, image=record_btn_img, command=record, borderwidth=0)
    record_btn.place(x=10, y=10)

    stop_btn_img = tkinter.PhotoImage(file='stop.png')
    stop_btn_lbl = tkinter.Label(image=stop_btn_img)
    stop_btn = tkinter.Button(window, image=stop_btn_img, command=stop, borderwidth=0)
    stop_btn['state'] = DISABLED
    stop_btn.place(x=55, y=12)

    recording_name = tkinter.Text(window, width=17, height=1)
    recording_name.insert(tkinter.INSERT, '')
    recording_name.place(x=100, y=15)

    window.mainloop()

detectorT = threading.Thread(target=detector.detect)
controlsT = threading.Thread(target=controls)

detectorT.start()
controlsT.start()