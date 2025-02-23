import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic

class CirclePainter(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for x, y, diameter in self.circles:
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(x, y, diameter, diameter)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.circle_painter = CirclePainter()
        self.setCentralWidget(self.circle_painter)

        self.btn.clicked.connect(self.circle_painter.add_circle)
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.circle_painter)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())