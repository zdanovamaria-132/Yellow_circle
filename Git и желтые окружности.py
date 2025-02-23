import sys
from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor

class CirclePainter(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def add_circle(self):
        diameter = randint(10, 100)
        x = randint(0, self.width() - diameter)
        y = randint(0, self.height() - diameter)
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        self.circles.append((x, y, diameter, r, g, b))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for x, y, diameter, r, g, b in self.circles:
            painter.setBrush(QColor(r, g, b))
            painter.drawEllipse(x, y, diameter, diameter)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Создание окружностей")
        self.setGeometry(100, 100, 600, 400)

        self.circle_painter = CirclePainter()
        self.setCentralWidget(self.circle_painter)

        self.btn = QPushButton("Добавить окружность", self)
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