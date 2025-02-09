import matplotlib.pyplot as plt
import numpy as np

# Example of basic bar chart
class ExampleBar:
    def __init__(self):
        self.x = np.array(["A", "B", "C", "D"])
        self.y = np.array([3, 8, 1, 10])

    def plot_vertical(self):
        plt.bar(self.x, self.y)
        plt.show()

    def plot_horizontal(self):
        plt.barh(self.x, self.y)
        plt.show()

# 創建 ExampleBar 物件
example_bar = ExampleBar()
# 呼叫 plot_vertical() 方法來繪製圖形
example_bar.plot_vertical()
# 呼叫 plot_horizontal() 方法來繪製圖形
example_bar.plot_horizontal()

# Set color by name or Hexadecimal 
class PlotColor:
    def __init__(self):
        self.x = np.array(["A", "B", "C", "D"])
        self.y = np.array([3, 8, 1, 10])

    def plot_color_name(self):
        plt.bar(self.x, self.y, color = "hotpink")
        plt.show()

    def plot_color_HEX(self):
        plt.bar(self.x, self.y, color = "#4CAF50")
        plt.show()

# 創建 PlotColor 物件
plot_color = PlotColor()
# 呼叫 plot_color_name() 方法來繪製圖形
plot_color.plot_color_name()
# 呼叫 plot_color_HEX() 方法來繪製圖形
plot_color.plot_color_HEX()

# Set the width of the bars
class BarWidth:
    def __init__(self):
        self.x = np.array(["A", "B", "C", "D"])
        self.y = np.array([3, 8, 1, 10])

    def plot_vert_width(self):
        plt.bar(self.x, self.y, width = 0.1)
        plt.show()

    def plot_hori_width(self):
        plt.barh(self.x, self.y, height = 0.1)
        plt.show()

# 創建 BarWidth 物件
bar_width = BarWidth()
# 呼叫 plot_vert_width() 方法來繪製圖形
bar_width.plot_vert_width()
# 呼叫 plot_hori_width() 方法來繪製圖形
bar_width.plot_hori_width()

