# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 20:20:14 2023

@author: DevOps
"""
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication,QMainWindow, QPushButton, QLineEdit, QHBoxLayout, QWidget, QVBoxLayout, QLabel
from pytube import YouTube

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Video DownLoader")
        self.button = QPushButton("Download")
        self.button.clicked.connect(self.the_button_was_clicked)
        
        
        self.inputBox = QLineEdit()
        layout = QHBoxLayout()
        layout.addWidget(self.inputBox)
        layout.addWidget(self.button)
        
        self.destPath = QLineEdit()
        self.pathLabel = QLabel("Destinition Path:")
        layout1 = QHBoxLayout()
        layout1.addWidget(self.pathLabel)
        layout1.addWidget(self.destPath)
    
        
        
        
        layout2 = QVBoxLayout()
        layout2.addLayout(layout)
        layout2.addLayout(layout1)
        
        widget = QWidget()
        widget.setLayout(layout2)
        
       
       
           

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
        
    def the_button_was_clicked(self):
        yt = YouTube(self.inputBox.text())
        yd = yt.streams.get_highest_resolution()
        yd.download(str(self.destPath.text()))
app = QApplication([])

window = MainWindow()
window.show()
app.exec()
