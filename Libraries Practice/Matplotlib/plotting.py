import matplotlib.pyplot as plt
import numpy as np

# Example for basic plot() function：Written in OOP
class ExamplePlot:
    def __init__(self):
        self.x = np.array([1, 8])
        self.y = np.array([3, 10])
        
    def plot_in_line(self):
        """ 繪製線條 """
        plt.plot(self.x, self.y)
        plt.show()

    def plot_in_point(self):
        """ 繪製點 """
        plt.plot(self.x, self.y, 'o')
        plt.show()

# 創建 ExamplePlot 物件
example_plot = ExamplePlot()
# 呼叫 plot_in_line() 方法來繪製圖形
example_plot.plot_in_line()
# 呼叫 plot_in_point() 方法來繪製圖形
example_plot.plot_in_point()

# Draw multiple points：Written in OOP
class MultiplePoints:
    def __init__(self):
        self.x = np.array([1, 2, 6, 8])
        self.y = np.array([3, 8, 1, 10])
        
    def plot(self):
        plt.plot(self.x, self.y)
        plt.show()

# 創建 ExamplePlot 物件
multi_points_plot = MultiplePoints()
# 呼叫 plot_in_line() 方法來繪製圖形
multi_points_plot.plot()

# Plot with default x points
class DefaultX:
    def __init__(self):
        self.y = np.array([3, 8, 1, 10, 5, 7])
        
    def plot(self):
        """ 僅給予Y值繪圖 """
        plt.plot(self.y)
        plt.show()

# 創建 DefaultX 物件
default_x_points = DefaultX()
# 呼叫 plot_in_line() 方法來繪製圖形
default_x_points.plot()









