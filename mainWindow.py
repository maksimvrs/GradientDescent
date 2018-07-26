from PyQt5.QtChart import *
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from gradient import GradientDescent


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.grad = None

        self.series = QLineSeries()

        pen = QPen()
        pen.setStyle(Qt.DashDotLine)
        pen.setWidth(10)
        pen.setBrush(Qt.darkBlue)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        self.series.setPen(pen)

        self.point = QScatterSeries()
        self.point.setMarkerShape(QScatterSeries.MarkerShapeCircle)
        self.point.setMarkerSize(10)
        self.point.setColor(QColor(Qt.darkGreen))

        self.chart = QChart()
        self.chart.legend().hide()

        main_layout = QVBoxLayout()

        view = QChartView(self.chart)
        view.setRenderHint(QPainter.Antialiasing)
        main_layout.addWidget(view)

        func_layout = QHBoxLayout()
        func_layout.addWidget(QLabel('f(x) = '))
        line_edit = QLineEdit()
        func_layout.addWidget(line_edit)
        main_layout.addLayout(func_layout)

        button = QPushButton('Начать оптимизацию')
        button.clicked.connect(lambda: self.start(line_edit.text()))
        main_layout.addWidget(button)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def set_title(self, title):
        self.chart.setTitle(title)

    def plot_2d(self, x, y, color=None):
        pen = self.series.pen()
        if color is not None:
            pen.setColor(color)
        pen.setWidthF(.1)
        self.series.setPen(pen)
        self.series.setUseOpenGL(True)

        self.series.append(map(QPointF, x, y))

        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()

    def set_point(self, x, y):
        self.point.clear()
        self.point.append(QPointF(x, y))
        self.chart.addSeries(self.point)

    def start(self, func):
        self.grad = GradientDescent(func, 3, 9, parent=self)
        self.grad.step_signal.connect(lambda x, y: self.set_point(x, y))
        self.grad.optimize()
