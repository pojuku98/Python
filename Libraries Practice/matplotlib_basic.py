# Matplotlib 是 Python 的可視化庫，提供靈活的繪圖功能，
# 可用於生成折線圖、柱狀圖、散點圖、熱圖等多種圖表，廣泛應用於數據分析與科學計算。

# 2-5-1
# seaborn能讓圖表更美觀
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np
import numpy.random as random

# 2-5-2-1
# 散布圖：以物件導向設計
class ScatterPlot:
    def __init__(self, seed=0, num_points=30, figsize=(20,6)):
        """ 初始化散布圖屬性 """
        random.seed(seed)                                       # 固定種子值
        self.x = random.randn(num_points)                       # 給定x軸資料
        self.y = np.sin(self.x) + random.randn(num_points)      # 給定y軸資料
        self.figsize = figsize
        self.title = "Title Name: Scatter"
        self.xlabel = "X"
        self.ylabel = "Y"
        self.grid = True

    def plot(self):
        """ 繪製散布圖 """
        plt.figure(figsize=self.figsize)                        # 指定圖形的大小
        plt.scatter(self.x, self.y)                             # 使用 scatter() 繪製散布圖
        # 也能如下描繪散布圖，'o'意指描點
        # plt.plot(x, y, 'o')
        plt.title(self.title)                                   # 標題
        plt.xlabel(self.xlabel)                                 # X軸標籤
        plt.ylabel(self.ylabel)                                 # Y軸標籤
        plt.grid(self.grid)                                     # 顯示grid (圖形中的格線)
        plt.show()                                              # 印出圖表
        
# 創建 ScatterPlot 物件
scatter = ScatterPlot()
# 呼叫 plot() 方法來繪製圖形
scatter.plot()

# 2-5-2-2
# 折線圖：連續曲線，以物件導向設計
class LinePlot:
    def __init__(self, seed=0, range=1000, figsize=(20,6), label = 'Label'):
        """ 初始化折線圖屬性 """
        random.seed(seed)                               # 固定種子值
        self.x = np.arange(range)                       # 資料範圍
        self.y = random.randn(range).cumsum()           # 生成亂數與累積和
        self.figsize = figsize
        self.label = label
        self.title = "Title Name: Line Chart"
        self.xlabel = "X"
        self.ylabel = "Y"
        self.grid = True

    def plot(self):
        """ 繪製折線圖 """
        plt.figure(figsize=self.figsize)                # 指定圖形的大小
        plt.plot(self.x, self.y, label=self.label)      # 使用 plot() 繪製折線圖，參數label用來指定圖例的名稱
        plt.legend()                                    # 顯示圖例
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid(self.grid)
        plt.show()

# 創建 LinePlot 物件
line_chart = LinePlot()
line_chart.plot()

# 2-5-3
# 分割圖：以物件導向設計
class SubPlot:
    def __init__(self, figsize=(20, 6), row=2, col=1, 
                 start=-10, stop=10, count=100):
        """ 初始化分割圖屬性 """
        self.figsize = figsize
        self.title = "Title Name: Subplot"
        self.row = row
        self.col = col

        self.x_1 = np.linspace(start, stop, count)      # 生成在指定範圍內的等間距數值陣列
        self.y_1 = np.sin(self.x_1)

        self.x_2 = self.x_1
        self.y_2 = np.sin(2 * self.x_2)
        
        self.grid = True

    def plot(self):
        """ 繪製分割圖 """
        plt.figure(figsize=self.figsize)                # 指定圖形的大小
        plt.title(self.title)

        plt.subplot(self.row, self.col, 1)              # 2列1行圖形的第1個
        plt.plot(self.x_1, self.y_1)

        plt.subplot(self.row, self.col, 2)              # 2列1行圖形的第2個
        plt.plot(self.x_2, self.y_2)

        plt.grid(self.grid)
        plt.show()

# 創建 SubPlot 物件
subplot = SubPlot()
subplot.plot()

# 2-5-4
# 描繪函數圖形，還不是很完美的解法
class FunctionPlot:
    def __init__(self, figsize=(20, 6)):
        """ 初始化函數圖屬性 """
        self.x = np.arange(-10, 10)
        self.figsize = figsize
        self.title = "Title Name: Function Plot"
        self.xlabel = "X"
        self.ylabel = "Y"
        self.grid = True

    def myFunction(self, x):
        """ 函數的定義 """
        return ( x**2 + 2*x + 1 )
    
    def plot(self):
        """ 繪製函數圖 """
        plt.figure(figsize=self.figsize)
        plt.plot(self.x, self.myFunction(self.x))
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid(self.grid)
        plt.show()

# 創建 FunctionPlot 物件
function_plot = FunctionPlot()
function_plot.plot()

# 2-5-5
# 直方圖
class Histogram:
    def __init__(self, seed=0, figsize=(20, 6), range=(20, 80)):
        random.seed(seed)                                           # 固定種子值
        self.figsize = figsize
        self.data = random.randn(10 ** 5) * 10 + 50
        self.bins = range[1] - range[0]                             # 60
        self.range = range
        self.title = "Title Name: Histogram"
        self.xlabel = "X"
        self.ylabel = "Y"
        self.grid = True

    def plot(self):
        plt.figure(figsize=self.figsize)                            # 指定圖形的大小
        plt.hist(self.data, bins=self.bins, range=self.range)       # 描繪直方圖
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid(self.grid)
        plt.show()

# 創建 Histogram 物件
histogram = Histogram()
histogram.plot()
