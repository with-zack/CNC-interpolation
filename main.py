import dda
import sys
import matplotlib.pyplot as plt
from matplotlib import animation
from PyQt5 import uic, QtWidgets

qtCreatorFile = "gui.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.line_interpolation.clicked.connect(self.dda_line)
        self.arc_interpolation.clicked.connect(self.dda_arc)

    def dda_line(self):
        x0 = float(self.x0_input.toPlainText())
        y0 = float(self.y0_input.toPlainText())
        xe = float(self.xe_input.toPlainText())
        ye = float(self.ye_input.toPlainText())
        x_coordinates, y_coordinates, output_string, m = dda.dda_line(x0, y0, xe, ye)

        self.results_window.setText(output_string)

        # First set up the figure, the axis, and the plot element we want to animate
        fig = plt.figure()
        plt.title("dda line interpolation")

        # 设置合适坐标轴
        if x0 > xe:
            x_start = xe - abs(x0-xe)/10
            x_end = x0 + abs(x0-xe)/10
        if x0 < xe:
            x_start = x0 - abs(x0-xe)/10
            x_end = xe + abs(x0-xe)/10
        if x0 == xe:
            x_start = x0 - 5
            x_end = x0 + 5
        if y0 > ye:
            y_start = ye - abs(y0-ye)/10
            y_end = y0 + abs(y0-ye)/10
        if y0 < ye:
            y_start = y0 - abs(y0-ye)/10
            y_end = ye + abs(y0-ye)/10
        if y0 == ye:
            y_start = y0 - 5
            y_end = y0 + 5

        ax = plt.axes(xlim=(x_start, x_end), ylim=(y_start, y_end))
        line, = ax.plot([], [], lw=2)
        plt.plot([x0, xe], [y0, ye], 'g')
        plt.scatter([x0, xe], [y0, ye])
        # initialization function: plot the background of each frame

        def init():
            line.set_data([], [])
            return line,

        # animation function.  This is called sequentially
        def animate(i):
            if i < len(x_coordinates):
                x = [x_coordinates[0:i]]
                y = [y_coordinates[0:i]]
            else:
                x = x_coordinates
                y = y_coordinates
            line.set_data(x, y)
            return line,

        # call the animator.  blit=True means only re-draw the parts that have changed.
        anim = animation.FuncAnimation(fig, animate, init_func=init,
                                       frames=m*20, interval=30, blit=True)

        plt.show()

    def dda_arc(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
