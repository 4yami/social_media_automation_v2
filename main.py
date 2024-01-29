from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QCoreApplication 

QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()

        # Load the UI file
        ui_file = QFile('home.ui')
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        try:
            loader.load(ui_file, self)
        except Exception as e:
            print(f"Error loading UI file: {e}")
        ui_file.close()

if __name__ == '__main__':
    app = QApplication([])
    window = HomeWindow()
    window.show()
    app.exec()
