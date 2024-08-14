import sys
from PyQt6.QtWidgets import QApplication, QWidget
from components.mainWindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow()

sys.exit(app.exec())
