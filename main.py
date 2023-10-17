from PyQt6.QtWidgets import QApplication
from widgets.calc import MainWindow
from sys import argv

if __name__ == "__main__":
    app = QApplication(argv)
    mn = MainWindow(240, 295)
    mn.show()
    exit(app.exec())