import numpy as np
import matplotlib.pyplot as plt

# Use the grid() function to add grid lines to the plot.
class ExampleGrid:
    def __init__(self):
        self.x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
        self.y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

    def plot(self):
        plt.title("Sports Watch Data")
        plt.xlabel("Average Pulse")
        plt.ylabel("Calorie Burnage")

        plt.plot(self.x, self.y)

        plt.grid()

        plt.show()

# 創建 ExampleGrid 物件
example_grid = ExampleGrid()
# 呼叫 plot() 方法來繪製圖形
example_grid.plot()

# Specify which grid lines to display.
class SpecifyGridLine:
    def __init__(self):
        self.x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
        self.y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

        self.title = "Sports Watch Data"
        self.xlabel = "Average Pulse"
        self.ylabel = "Calorie Burnage"

    def plot_x_axis(self):
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        plt.plot(self.x, self.y)

        plt.grid(axis = 'x')

        plt.show()

    def plot_y_axis(self):
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        plt.plot(self.x, self.y)

        plt.grid(axis = 'y')

        plt.show()

# 創建 SpecifyGridLine 物件
grid_axis = SpecifyGridLine()
# 呼叫 plot_x_axis() 方法來繪製圖形
grid_axis.plot_x_axis()
# 呼叫 plot_y_axis() 方法來繪製圖形
grid_axis.plot_y_axis()

# Set the line properties of the grid
class GridProperty:
    def __init__(self):
        self.x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
        self.y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

        self.title = "Sports Watch Data"
        self.xlabel = "Average Pulse"
        self.ylabel = "Calorie Burnage"

    def plot(self):
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        plt.plot(self.x, self.y)

        plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

        plt.show()

# 創建 GridProperty 物件
grid_prop = GridProperty()
# 呼叫 plot() 方法來繪製圖形
grid_prop.plot()

