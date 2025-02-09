import matplotlib.pyplot as plt
import numpy as np

# Focus on variety of linestyle
class FocusLinestyle:
    def __init__(self):
        self.y = np.array([3, 8, 1, 10])

    def plot_dot(self):
        plt.plot(self.y, linestyle = 'dotted')
        plt.show()

    def plot_dash(self):
        plt.plot(self.y, linestyle = 'dashed')
        plt.show()

# 創建 FocusLinestyle 物件
focus_linestyle = FocusLinestyle()
# 呼叫 plot_dot() 方法來繪製圖形
focus_linestyle.plot_dot()
# 呼叫 plot_dash() 方法來繪製圖形
focus_linestyle.plot_dash()

# Focus on line color
class LineColor:
    def __init__(self):
        self.y = np.array([3, 8, 1, 10])

    def plot_color_short(self):
        plt.plot(self.y, color = 'r')
        plt.show()

    def plot_color_hex(self):
        plt.plot(self.y, color = '#4CAF50')
        plt.show()

    def plot_color_name(self):
        plt.plot(self.y, color = 'hotpink')
        plt.show()

# 創建 LineColor 物件
line_color = LineColor()
# 呼叫 plot_color_short() 方法來繪製圖形
line_color.plot_color_short()
# 呼叫 plot_color_hex() 方法來繪製圖形
line_color.plot_color_hex()
# 呼叫 plot_color_name() 方法來繪製圖形
line_color.plot_color_name()

# Focus on line width
class LineWidth:
    def __init__(self):
        self.y = np.array([3, 8, 1, 10])

    def plot_width(self):
        plt.plot(self.y, linewidth = '20.5')
        plt.show()

# 創建 LineWidth 物件
line_width = LineWidth()
# 呼叫 plot_width() 方法來繪製圖形
line_width.plot_width()

# Multiple lines
class MultipleLine:
    def __init__(self):
        self.x_1 = np.array([0, 1, 2, 3])
        self.y_1 = np.array([3, 8, 1, 10])
        self.x_2 = np.array([0, 1, 2, 3])
        self.y_2 = np.array([6, 2, 7, 11])

    def plot_more_line(self):
        plt.plot(self.y_1)
        plt.plot(self.y_2)

        plt.show()

    def plot_more_point(self):
        plt.plot(self.x_1, self.y_1, 
                 self.x_2, self.y_2)
        plt.show()

# 創建 MultipleLine 物件
multiple_line = MultipleLine()
# 呼叫 plot_more_line() 方法來繪製圖形
multiple_line.plot_more_line()
# 呼叫 plot_more_point() 方法來繪製圖形
multiple_line.plot_more_point()




