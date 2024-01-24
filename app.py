import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        # Set the dark theme
        self.set_dark_theme()

        # Create a button to demonstrate
        button = QPushButton("Click me!", self)
        button.clicked.connect(self.on_button_click)

        # Set up the main window
        self.setWindowTitle("My App")

    def set_dark_theme(self):
        # Set the application style to Fusion
        QApplication.setStyle("Fusion")
        # Set a dark color palette
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(dark_palette)

    def on_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dark_theme_app = MyApp()
    
    # Maximize the window
    dark_theme_app.showMaximized()

    sys.exit(app.exec())
