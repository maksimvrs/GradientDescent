import tensorflow as tf
from PyQt5.QtCore import QObject, pyqtSignal


class GradientDescent(QObject):
    step_signal = pyqtSignal(int, int, name='stepChanged')

    def __init__(self, func, x_init=0, y_init=0, parent=None):
        super(GradientDescent, self).__init__(parent=parent)
        self.learning_rate = 0.5
        self.func_string = func
        x = tf.Variable(x_init, name='x', dtype=tf.float32)
        # y = tf.Variable(y_init, name='y', dtype=tf.float32)
        try:
            self.func = eval(func)
            self.x = x
            # self.y = y
        except (ValueError, SyntaxError):
            pass

    def optimize(self):
        optimizer = tf.train.GradientDescentOptimizer(self.learning_rate)
        train = optimizer.minimize(self.func)
        init = tf.global_variables_initializer()
        with tf.Session() as session:
            session.run(init)
            for step in range(10):
                session.run(train)
                x, y = session.run([self.x, self.func])
                self.step_signal.emit(x, y)
