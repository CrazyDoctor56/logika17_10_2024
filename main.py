from PyQt6.QtWidgets import QApplication, QMainWindow
from ui import Ui_Dialog


app = QApplication([])
win = QMainWindow()

ui = Ui_Dialog()

ui.setupUi(win)

current_number = 0

def increase_number():
    global current_number
    current_number += 1
    ui.number.setText(str(current_number))

ui.btn.clicked.connect(increase_number)

win.show()
app.exec()