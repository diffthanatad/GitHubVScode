from Simple_drawing_window1 import Simple_drawing_window as win1
from Simple_drawing_window2 import Simple_drawing_window as win2
from Simple_drawing_window3 import Simple_drawing_window as win3

import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

def main():
    app = QApplication(sys.argv)

    w1 = win1()
    w2 = win2()
    w3 = win3()
    
    w1.show()
    w2.show()
    w3.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
