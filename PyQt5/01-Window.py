import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import os

current_dir = os.path.dirname(__file__)
image_path_1 = os.path.join(current_dir,"Images", "Legion Logo.jpg")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI lowkey, well ackshauly no")
        self.setGeometry(0, 0, 900, 900) # (x,y,width,height) x,y at 0 makes window appear at upper left corner of screen
        self.setWindowIcon(QIcon(image_path_1))

def main():
    app = QApplication(sys.argv) # by passing sys.argv, it allows pyqt to proccess any command line arguments intended for it
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # exec_ is a excecute method, it waits around for user inputs and handles user event

if __name__=="__main__":
    main()