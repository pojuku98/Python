import matplotlib.pyplot as plt
import numpy as np

# Example of basic subplot()：1 row, 2 columns
class ExampleSubplot:
    def __init__(self):
        self.super_title = "MY SHOP"
        self.row = 1
        self.col = 2

        """ plot 1 """
        self.title_1 = "SALES"
        self.x_1 = np.array([0, 1, 2, 3])
        self.y_1 = np.array([3, 8, 1, 10])

        """ plot 2 """
        self.title_2 = "INCOME"
        self.x_2 = np.array([0, 1, 2, 3])
        self.y_2 = np.array([10, 20, 30, 40])

    def plot(self):

        """ plot 1 """
        plt.subplot(self.row, self.col, 1)
        plt.plot(self.x_1, self.y_1)
        plt.title(self.title_1)

        """ plot 2 """
        plt.subplot(self.row, self.col, 2)
        plt.plot(self.x_2, self.y_2)
        plt.title(self.title_2)

        plt.suptitle(self.super_title)
        plt.show()

# 創建 ExampleSubplot 物件
example_subplt = ExampleSubplot()
# 呼叫 plot() 方法來繪製圖形
example_subplt.plot()

# Draw as many plots
class MultiPlots:
    def __init__(self):
        self.nrows = 2
        self.ncols = 3
        self.figsize = (10, 6)

        self.x_1 = np.array([0, 1, 2, 3])
        self.y_1 = np.array([3, 8, 1, 10])

        self.x_2 = np.array([0, 1, 2, 3])
        self.y_2 = np.array([10, 20, 30, 40])

    def select_data(self, i, j):
        """ SRP. Only select data, don't draw. """
        return (self.x_1, self.y_1) if (i+j) % 2 == 0 else (self.x_2, self.y_2)
        
    def plot(self):
        self.fig, self.ax = plt.subplots(nrows=self.nrows, ncols=self.ncols, figsize=self.figsize)

        for i in range(self.nrows):
            for j in range(self.ncols):
                """ According to SRP(單一職責原則), seperate select data and draw. """
                x, y = self.select_data(i, j)
                self.ax[i, j].plot(x, y)
                
        plt.show()

# 創建 MultiPlots 物件
multi_subplt = MultiPlots()
# 呼叫 plot() 方法來繪製圖形
multi_subplt.plot()













"""
    self.ax[0, 0].plot(self.x_1, self.y_1)
    self.ax[0, 1].plot(self.x_2, self.y_2)
    self.ax[0, 2].plot(self.x_1, self.y_1)
    self.ax[1, 0].plot(self.x_2, self.y_2)
    self.ax[1, 1].plot(self.x_1, self.y_1)
    self.ax[1, 2].plot(self.x_2, self.y_2)
"""

"""    
    if (i+j) % 2 == 0:
        return self.x_1, self.y_1
    else:
        return self.x_2, self.y_2
"""