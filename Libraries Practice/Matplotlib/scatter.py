import matplotlib.pyplot as plt
import numpy as np

# Example of basic scatter
class ExampleScatter:
    def __init__(self):
        self.x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
        self.y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

    def plot(self):
        plt.scatter(self.x, self.y)
        plt.show()

# 創建 ExampleScatter 物件
example_scatter = ExampleScatter()
# 呼叫 plot() 方法來繪製圖形
example_scatter.plot()

# Compare two scatter plots
class ComparePlots:
    def __init__(self):

        """ day one, the age and speed of 13 cars """
        self.x_1 = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
        self.y_1 = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

        """ day two, the age and speed of 15 cars """
        self.x_2 = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
        self.y_2 = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

    def plot(self):

        """ day 1 """
        plt.scatter(self.x_1, self.y_1)

        """ day 2 """
        plt.scatter(self.x_2, self.y_2)

        plt.show()

    def plot_color(self):

        """ day 1 """
        plt.scatter(self.x_1, self.y_1, color = 'hotpink')

        """ day 2 """
        plt.scatter(self.x_2, self.y_2, color = '#88c999')

        plt.show()

# 創建 ComparePlots 物件
compare_scatter = ComparePlots()
# 呼叫 plot() 方法來繪製圖形
compare_scatter.plot()
# 呼叫 plot_color() 方法來繪製圖形
compare_scatter.plot_color()

# Set a specific color for each dot
class EachColor:
    def __init__(self):
        self.x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
        self.y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
        self.colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

    def plot(self):
        plt.scatter(self.x, self.y, c=self.colors)

        plt.show()

# 創建 EachColor 物件
each_color = EachColor()
# 呼叫 plot() 方法來繪製圖形
each_color.plot()

# Use colormap by cmap and colorbar
class ColorMap:
    def __init__(self):
        self.x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
        self.y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
        self.colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

    def plot(self):
        plt.scatter(self.x, self.y, c=self.colors, cmap='viridis')

        plt.colorbar()

        plt.show()

# 創建 ColorMap 物件
color_map = ColorMap()
# 呼叫 plot() 方法來繪製圖形
color_map.plot()

# Change the size of the dots
class DotsSize:
    def __init__(self):
        self.x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
        self.y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
        self.sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

    def plot(self):
        plt.scatter(self.x, self.y, s=self.sizes)

        plt.show()

# 創建 DotsSize 物件
dots_size = DotsSize()
# 呼叫 plot() 方法來繪製圖形
dots_size.plot()

# Adjust the transparency of the dots
class DotsTransparency:
    def __init__(self):
        self.x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
        self.y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
        self.sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

    def plot(self):
        plt.scatter(self.x, self.y, s=self.sizes, alpha=0.5)

        plt.show()

# 創建 DotsTransparency 物件
dots_alpha = DotsTransparency()
# 呼叫 plot() 方法來繪製圖形
dots_alpha.plot()

# Combine Color, Size, and Alpha
class ColorSizeAlpha:
    def __init__(self):
        self.x = np.random.randint(100, size=(100))
        self.y = np.random.randint(100, size=(100))
        self.colors = np.random.randint(100, size=(100))
        self.color_map = 'nipy_spectral'
        self.sizes = 10 * np.random.randint(100, size=(100))
        self.alpha = 0.5

    def plot(self):
        plt.scatter(self.x, self.y, 
                    c=self.colors, cmap=self.color_map, s=self.sizes, alpha=self.alpha)

        plt.colorbar()

        plt.show()

# 創建 ColorSizeAlpha 物件
color_size_alpha = ColorSizeAlpha()
# 呼叫 plot() 方法來繪製圖形
color_size_alpha.plot()




