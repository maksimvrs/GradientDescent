import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from mainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Градиентный спуск")

    x = []
    y = []
    for i in range(-10, 11):
        x.append(i)
        y.append(i ** 2)
    window.plot_2d(x, y)
    window.set_point(3, 9)

    window.show()
    window.resize(500, 400)
    sys.exit(app.exec_())
    # gradient_descent = GradientDescent("x ** 2")
