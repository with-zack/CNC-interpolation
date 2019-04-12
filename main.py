'''
2019/4/8
数字积分插补法DDA
实现功能:
1、输入起点与终点，进行自动直线插补和圆弧插补，并显示计算过程和路径
2、实现调速
3、圆弧插补可选顺逆时针与插补半径
'''
import math
import sys                       # 导入"system"模块，程序结尾有"sys.exit()"退出指令
import dda                       # 数值微分算法 DDA Digital Differential Analyzer
import matplotlib.pyplot as plt  # "matplotlib"2D绘图库 "pyplot"提供类似MATLAB的绘图框架
from matplotlib import animation # "animation"画动态图
from PyQt5 import uic, QtWidgets # "PyQt5"绘制界面

qtCreatorFile = "gui.ui"         # Enter file here.

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
        ani_speed = 100 - self.speed.value()
        
        x_coordinates, y_coordinates, output_string, m = dda.dda_line(x0, y0, xe, ye)

        self.output.setText(output_string)

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
                                       frames=m*20, interval=ani_speed, blit=True)

        plt.show()

    def dda_arc(self):
        x0 = float(self.x0_input.toPlainText())
        y0 = float(self.y0_input.toPlainText())
        xe = float(self.xe_input.toPlainText())
        ye = float(self.ye_input.toPlainText())
        R_input = float(self.R_input.toPlainText())
        ani_speed = 100 - self.speed.value()
        x_coordinates, y_coordinates, output_string, m = dda.dda_arc(x0, y0, xe, ye,R_input)

        self.output.setText(output_string)

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
                                       frames=m*20, interval=ani_speed, blit=True)
        print(x_coordinates)
        print(y_coordinates)
        plt.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
