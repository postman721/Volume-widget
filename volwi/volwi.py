#!/usr/bin/env python
#Volume widget Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#Volume widget comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991"

from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
import os, sys, subprocess
from subprocess import Popen

class Second(QWidget):
    def __init__(self, parent):
        super(Second, self).__init__(parent)
#Label.        
        self.label = QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color:#f1ff0e; background-color:#6b6b6b; font-size: 16px;")                      

#Make Layout.
        self.adjustSize() 
        self.mainLayout = QHBoxLayout(self)
        self.mainLayout.addWidget(self.label)
        
#Check label value and update it every n milliseconds.                    
    def changeLabel(self):
        #Volume
        self.initial1=subprocess.Popen(['bash', 'mixer.sh'], stdout=subprocess.PIPE) #Using Popen and piping subprocess to standard output.
        self.initial2=self.initial1.stdout.read() #Reading the standard output.
        self.initial3=int(self.initial2) #Changing to integrer.                 
        #Set Label text
        self.level= "Volume: " + str(self.initial3)+"%"
        self.label.setText(self.level)
        #Set texts.
        if self.initial3 > 100:
            self.over="Warning: " + str(self.initial3)+"%"			
            self.label.setText(self.over)
        
        elif self.initial3 == 0:
            self.over="Silence: " + str(self.initial3)+"%"			
            self.label.setText(self.over)   
    
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
#Notice that QMainWindow is parent of QWidget. This is a bit implicit but that 
#is how it goes by default. MainWindow is the parent of QWidget - since MainWindow is the main thing here
#and it does not declare (parent) in __init__.
        		
#Set window title. Set window style.		
        self.setWindowTitle("VolWi")
        self.setStyleSheet("color:#ffffff; background-color:#6b6b6b;font-size: 12px;")

#Set MainWindow Size attributes and remove the frame.		
        self.setMinimumSize(QtCore.QSize(145, 40))
        self.setMaximumSize(QtCore.QSize(145, 40))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #Frameless window declaration.

#Set geometry and move the window.
        #self.geometry(left coordinate, top coordinate. object width, object height).
        self.left=20
        self.top=40
        self.w=140
        self.h=60 
        self.setGeometry(self.left, self.top, self.w, self.h)

#Secondary layout & childWindow declarations.
#If we would not declare childWindow then keypress events would not launch -> From the second(class). Right now we have no keypresses
#coming from second(class) but this might change in the future.        
        self.secondLayout = QHBoxLayout()
        self.childWindow = Second(self)

#Timer to check changelabel function every n milliseconds.
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.childWindow.changeLabel)
        self.timer.start(100) #Update every 100 milliseconds.                         

#Add childWindow to layout of this window.  
        self.secondLayout.addWidget(self.childWindow)
        self.setCentralWidget(self.childWindow) #Set Label to become the central widget.

#Set focus to childWindow. -> important if we would pass keypresses from the second(class).
        self.childWindow.setFocus(True)
        self.adjustSize()

#Ignore ALT+F4. We want to avoid accidental closing.
    def closeEvent(self, event):
        event.ignore()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    sys.exit(app.exec_())
