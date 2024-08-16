from PyQt6.QtWidgets import (
    QPushButton,
)

class CustomButton(QPushButton):
    def mousePressEvent(self, e):
        self.parentWidget().mousePressEvent(e)
        
        super().mousePressEvent(e)