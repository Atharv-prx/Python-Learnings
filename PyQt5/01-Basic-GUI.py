import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

def main():
    app = QApplication(sys.argv) # by passing sys.argv, it allows pyqt to proccess any command line arguments intended for it
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # exec_ is a excecute method, it waits around for user inputs and handles user event

if __name__=="__main__":
    main()