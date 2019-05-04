from PySide2.QtWidgets import *
from PIL import Image
import imgfilters
import numpy as np

app = QApplication([])

img = Image.new("RGB", (1,1))

def OpenImage():
    global img
    img = Image.open(fileInput.text())

def Negate():
    global img 
    img = imgfilters.Negate(img)

def Show():
    global img
    img.show()

def Pixelize():
    global img
    img = imgfilters.Pixelate(img, int(sizeInput.text()))

def Grayscale():
    global img
    img = imgfilters.MakeGray(img)

def SimpleBlur():
    global img
    img = imgfilters.SimpleBlur(img, int(sizeInput.text()))

def EdgeDetect():
    global img
    img = imgfilters.EdgeDetect(img, int(sizeInput.text()))

fileInput = QLineEdit("Path to image")
sizeInput = QLineEdit("Pixelize & blur radius/Edge detection threshold")
nameInput = QLineEdit("New name")
btnNegate = QPushButton("Negate")
btnShow = QPushButton("Show")
btnOpen = QPushButton("Open")
btnGray = QPushButton("Grayscale")
btnPixelize = QPushButton("Pixelize")
btnBlur = QPushButton("Simple blur")
btnEdge = QPushButton("Edge detection")
btnSave = QPushButton("Save")
btnQuit = QPushButton("Quit")

btnNegate.clicked.connect(Negate)
btnShow.clicked.connect(Show)
btnOpen.clicked.connect(OpenImage)
btnGray.clicked.connect(Grayscale)
btnBlur.clicked.connect(SimpleBlur)
btnPixelize.clicked.connect(Pixelize)
btnEdge.clicked.connect(EdgeDetect)
btnSave.clicked.connect(lambda: img.save(nameInput.text() + ".bmp"))
btnQuit.clicked.connect(lambda: app.quit())

layout = QVBoxLayout()
layout.addWidget(fileInput)
layout.addWidget(sizeInput)
layout.addWidget(nameInput)
layout.addWidget(btnOpen)
layout.addWidget(btnShow)
layout.addWidget(btnNegate)
layout.addWidget(btnPixelize)
layout.addWidget(btnBlur)
layout.addWidget(btnGray)
layout.addWidget(btnEdge)
layout.addWidget(btnSave)
layout.addWidget(btnQuit)

window = QWidget()
window.setLayout(layout)
window.show()

app.exec_()




