import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt # used for allignments
import os

current_dir = os.path.dirname(__file__)
image_path_1 = os.path.join(current_dir,"Images", "Legion Logo.jpg")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 900, 900)
        self.setWindowTitle("Labels")

        label = QLabel("Sup", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0,0, 900, 100)
        label.setStyleSheet("color: #1fff5a;"
                            "background-color: #292929;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline; ")
        # label.setAlignment(Qt.AlignTop) # Vertically Top
        # label.setAlignment(Qt.AlignBottom) # Vertically Bottom
        #label.setAlignment(Qt.AlignVCenter) # Vertically center

        # label.setAlignment(Qt.AlignRight)  # HORIZONTALLY RIGHT
        #label.setAlignment(Qt.AlignHCenter)  # HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignLeft)  # HORIZONTALLY LEFT

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # CENTER & CENTER
        # label.setAlignment(Qt.AlignCenter)  # CENTER & CENTER

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 

if __name__=="__main__":
    main()