import sys

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load("widget.ui", None)

def do_something():
    print(window.full_name_line_edit.text(), "is a", window.occupation_line_edit.text())
    
window.setWindowTitle("User Data")
window.push_button.clicked.connect(do_something)
window.show()
app.exec()
