import numpy as np 
from numpy.fft import fft, ifft
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QSlider, QLabel
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from playsound import playsound
import os
import sys  
import wave, sys

ptr=0
selected_note='path'
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        #Load the UI Page
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('task3.ui', self)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.player = QMediaPlayer() # initializer
        self.action_open_2.triggered.connect(self.play_sound)
        self.timer.timeout.connect(self.signal_plot)
        self.pause_button.clicked.connect(self.pause)
        self.play_button.clicked.connect(self.replay)
        self.piano_label.mousePressEvent  = self.piano
        self.drums_label.mousePressEvent = self.drums
        self.xylo_label.mousePressEvent = self.xylophone
        # self.piano.connect(self.playinstrument)
        # self.drums.connect(self.playinstrument)
        # self.xylophone.connect(self.playinstrument)
        #define slider widget
        self.volume_slider = self.findChild(QSlider, "volume_slider")
        self.volume_number = self.findChild(QLabel, "volume_number")
        #move volume slider
        self.volume_number.setAlignment(QtCore.Qt.AlignCenter)
        self.volume_slider.valueChanged.connect(self.move_slider)
        self.volume_slider.setMaximum(100)

    def move_slider(self, value):
        self.volume_number.setText(str(value))



    def xylophone(self, event):
         x= event.pos().x()
         y= event.pos().y()

         if x/self.xylo_label.size().width() > 0.05 and x/self.xylo_label.size().width() < 0.14 and y/self.xylo_label.size().width() > 0.15 and y/self.xylo_label.size().width() < 0.30 :
            print("Bar 1") 
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Bar 1.wav'

    
         if x/self.xylo_label.size().width() > 0.16 and x/self.xylo_label.size().width() < 0.25 and y/self.xylo_label.size().width() > 0.13 and y/self.xylo_label.size().width() < 0.32 :
            print("Bar 2")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Bar 2.wav'


         if x/self.xylo_label.size().width() > 0.28 and x/self.xylo_label.size().width() < 0.37 and y/self.xylo_label.size().width() > 0.12 and y/self.xylo_label.size().width() < 0.33 :
            print("Bar 3")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Bar 3.wav'

         if x/self.xylo_label.size().width() > 0.40 and x/self.xylo_label.size().width() < 0.49 and y/self.xylo_label.size().width() > 0.1 and y/self.xylo_label.size().width() < 0.33 :
            print("Bar 4")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Bar 4.wav'

         if x/self.xylo_label.size().width() > 0.51 and x/self.xylo_label.size().width() < 0.60 and y/self.xylo_label.size().width() > 0.08 and y/self.xylo_label.size().width() < 0.36 :
            print("Bar 5")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Bar 5.wav'

         if x/self.xylo_label.size().width() > 0.63 and x/self.xylo_label.size().width() < 0.72 and y/self.xylo_label.size().width() > 0.05 and y/self.xylo_label.size().width() < 0.38 :
            print("Bar 6")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Bar 6.wav'

         if x/self.xylo_label.size().width() > 0.75 and x/self.xylo_label.size().width() < 0.84 and y/self.xylo_label.size().width() > 0.03 and y/self.xylo_label.size().width() < 0.4 :
            print("Bar 7")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Bar 7.wav'
        
         if x/self.xylo_label.size().width() > 0.86 and x/self.xylo_label.size().width() < 0.96 and y/self.xylo_label.size().width() > 0.2 and y/self.xylo_label.size().width() < 0.42 :
            print("Bar 8")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Bar 8.wav'


        #  print(x)
        #  print(y)

    
    def drums(self, event):
        x= event.pos().x()
        y= event.pos().y()
        if x/self.drums_label.size().width() > 0.027 and x/self.drums_label.size().width() < 0.26 and y/self.drums_label.size().width() > 0.009 and y/self.drums_label.size().width() < 0.07 :
            print("Ride Cymbal") 
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Ride Cymbal.wav'

        if x/self.drums_label.size().width() > 0.733 and x/self.drums_label.size().width() < 1.00 and y/self.drums_label.size().width() > 0.03 and y/self.drums_label.size().width() < 0.10 :
            print("Hi-Hat Cymbal") 
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Hi-Hat Cymbal.wav'

        if x/self.drums_label.size().width() > 0.53 and x/self.drums_label.size().width() < 0.69 and y/self.drums_label.size().width() > 0.10 and y/self.drums_label.size().width() < 0.25 :
            print("Medium Tom") 
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Medium Toml.wav'

        if x/self.drums_label.size().width() > 0.21 and x/self.drums_label.size().width() < 0.50 and y/self.drums_label.size().width() > 0.05 and y/self.drums_label.size().width() < 0.20 :
            print("High Tom")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/High Tom.wav'

        if x/self.drums_label.size().width() > 0.05 and x/self.drums_label.size().width() < 0.24 and y/self.drums_label.size().width() > 0.15 and y/self.drums_label.size().width() < 0.50 :
            print("Stand Tom") 
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Stand Tom.wav'

        if x/self.drums_label.size().width() > 0.41 and x/self.drums_label.size().width() < 0.72 and y/self.drums_label.size().width() > 0.30 and y/self.drums_label.size().width() < 1.0 :
            print("Bass Drum") 
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Bass Drum.wav'

        if x/self.drums_label.size().width() > 0.76 and x/self.drums_label.size().width() < 0.84 and y/self.drums_label.size().width() > 0.20 and y/self.drums_label.size().width() < 0.63 :
            print("Snare Drum") 
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Snare Drum.wav'
       

        # print(x)
        # print(y)
    

    def piano(self,event):
        x = event.pos().x()
        y = event.pos().y() 

        if x/self.piano_label.size().width() > 0.15 and x/self.piano_label.size().width() < 0.20  and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 1") 
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 1.wav'  

        if x/self.piano_label.size().width() > 0.20 and x/self.piano_label.size().width() < 0.25 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 2")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 2.wav'

        if x/self.piano_label.size().width() > 0.25 and x/self.piano_label.size().width() < 0.30 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 3")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 3.wav'

        if x/self.piano_label.size().width() > 0.30 and x/self.piano_label.size().width() < 0.35 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 4")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 4.wav'

        if x/self.piano_label.size().width() > 0.35 and x/self.piano_label.size().width() < 0.40 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 5")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 5.wav'

        if x/self.piano_label.size().width() > 0.40 and x/self.piano_label.size().width() < 0.45 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 6")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 6.wav'

        if x/self.piano_label.size().width() > 0.45 and x/self.piano_label.size().width() < 0.50 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 7")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 7.wav'

        if x/self.piano_label.size().width() > 0.50 and x/self.piano_label.size().width() < 0.55 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 8")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 1.wav'

        if x/self.piano_label.size().width() > 0.55 and x/self.piano_label.size().width() < 0.60 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 9")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 2.wav'

        if x/self.piano_label.size().width() > 0.60 and x/self.piano_label.size().width() < 0.65 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 10")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 3.wav'

        if x/self.piano_label.size().width() > 0.65 and x/self.piano_label.size().width() < 0.70 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 11")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 4.wav'

        if x/self.piano_label.size().width() > 0.70 and x/self.piano_label.size().width() < 0.75 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 12")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 5.wav'

        if x/self.piano_label.size().width() > 0.75 and x/self.piano_label.size().width() < 0.80 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 13")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 6.wav'

        if x/self.piano_label.size().width() > 0.80 and x/self.piano_label.size().width() < 0.85 and y/self.piano_label.size().width() > 0.30 and y/self.piano_label.size().width() < 0.40 :
            print("White Key 14")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/White Key 7.wav'

        if x/self.piano_label.size().width() > 0.18 and x/self.piano_label.size().width() < 0.22 and y/self.piano_label.size().width() > 0.10 and y/self.piano_label.size().width() < 0.29 :
            print("Black Key 1")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Black Key 1.wav'

        if x/self.piano_label.size().width() > 0.23 and x/self.piano_label.size().width() < 0.27 and y/self.piano_label.size().width() > 0.10 and y/self.piano_label.size().width() < 0.29 :
            print("Black Key 2")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Black Key 2.wav'

        if x/self.piano_label.size().width() > 0.34 and x/self.piano_label.size().width() < 0.37 and y/self.piano_label.size().width() > 0.10 and y/self.piano_label.size().width() < 0.29 :
            print("Black Key 3")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Black Key 3.wav'

        if x/self.piano_label.size().width() > 0.39 and x/self.piano_label.size().width() < 0.42 and y/self.piano_label.size().width() > 0.10 and y/self.piano_label.size().width() < 0.29 :
            print("Black Key 4")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Black Key 4.wav'

        if x/self.piano_label.size().width() > 0.44 and x/self.piano_label.size().width() < 0.47 and y/self.piano_label.size().width() > 0.10 and y/self.piano_label.size().width() < 0.29 :
            print("Black Key 5")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Black Key 5.wav'

        if x/self.piano_label.size().width() > 0.54 and x/self.piano_label.size().width() < 0.57 and y/self.piano_label.size().width() > 0.10 and y/self.piano_label.size().width() < 0.29 :
            print("Black Key 6")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Black Key 1.wav'

        if x/self.piano_label.size().width() > 0.59 and x/self.piano_label.size().width() < 0.62 and y/self.piano_label.size().width() > 0.10 and y/self.piano_label.size().width() < 0.29 :
            print("Black Key 7")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Black Key 2.wav'

        if x/self.piano_label.size().width() > 0.69 and x/self.piano_label.size().width() < 0.73 and y/self.piano_label.size().width() > 0.10 and y/self.piano_label.size().width() < 0.29 :
            print("Black Key 8")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Black Key 3.wav'

        if x/self.piano_label.size().width() > 0.74 and x/self.piano_label.size().width() < 0.78 and y/self.piano_label.size().width() > 0.10 and y/self.piano_label.size().width() < 0.29 :
            print("Black Key 9")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Black Key 4.wav'

        if x/self.piano_label.size().width() > 0.79 and x/self.piano_label.size().width() < 0.83 and y/self.piano_label.size().width() > 0.10 and y/self.piano_label.size().width() < 0.29 :
            print("Black Key 10")
            self.selected_note='C:/Users/Asus a/Desktop/DSP/task 3/github/Musical-Instruments-Emphasizer-equa/Black Key 5.wav'
       

        # print(x)
        # print(y)
    
    def play_sound(self):
        full_file_path = os.path.join(os.getcwd(), 'test.wav')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
        self.timer.start()
    
    def pause(self):
        self.player.pause()
        self.timer.stop()
    
    def replay(self):
        self.player.play()
        self.timer.start(500)
        
    def signal_plot(self):
        global ptr
        spf = wave.open("test.wav", "r")
        # Extract Raw Audio from Wav File
        signal = spf.readframes(-1)
        signal = np.frombuffer(signal, "int16")
        fs = spf.getframerate()
        time = np.linspace(0, len(signal) / fs, num=len(signal))
        
        self.mainsignal_widget.setYRange(min(signal),max(signal))
        self.mainsignal_widget.setXRange(0 + ptr, 1 + ptr)
        self.mainsignal_widget.plot(time, signal)
        ptr+=0.5

    def playinstrument(self):
        # for playing note.wav file
        playsound(self.selected_not)
        print('playing sound using  playsound')
        

               
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
