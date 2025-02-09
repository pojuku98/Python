import matplotlib.pyplot as plt
import numpy as np

# Example of basic pie chart
class ExamplePie:
    def __init__(self):
        self.y = np.array([35, 25, 25, 15])

    def plot(self):
        plt.pie(self.y)
        plt.show() 

# 創建 ExamplePie 物件
example_pie = ExamplePie()
# 呼叫 plot() 方法來繪製圖形
example_pie.plot()

# Add labels to the pie chart
class PieLabels:
    def __init__(self):
        self.y = np.array([35, 25, 25, 15])
        self.mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

    def plot(self):
        plt.pie(self.y, labels = self.mylabels)
        plt.show() 

# 創建 PieLabels 物件
pie_label = PieLabels()
# 呼叫 plot() 方法來繪製圖形
pie_label.plot()

# Change start angle
class StartAngle:
    def __init__(self):
        self.y = np.array([35, 25, 25, 15])
        self.mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
        self.startangle = 90

    def plot(self):
        plt.pie(self.y, labels = self.mylabels, startangle = self.startangle)
        plt.show() 

# 創建 StartAngle 物件
start_angle = StartAngle()
# 呼叫 plot() 方法來繪製圖形
start_angle.plot()

# wedges stand out
class Explode:
    def __init__(self):
        self.y = np.array([35, 25, 25, 15])
        self.mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
        self.myexplode = [0.2, 0, 0, 0]

    def plot(self):
        plt.pie(self.y, labels = self.mylabels, explode = self.myexplode)
        plt.show()

# 創建 Explode 物件
explode = Explode()
# 呼叫 plot() 方法來繪製圖形
explode.plot()

# Add a shadow to the pie chart
class PieShadow:
    def __init__(self):
        self.y = np.array([35, 25, 25, 15])
        self.mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
        self.myexplode = [0.2, 0, 0, 0]

    def plot(self):
        plt.pie(self.y, labels = self.mylabels, explode = self.myexplode, 
                shadow = True)
        plt.show()

# 創建 PieShadow 物件
pie_shadow = PieShadow()
# 呼叫 plot() 方法來繪製圖形
pie_shadow.plot()

# Set the color of each wedge
class PieColor:
    def __init__(self):
        self.y = np.array([35, 25, 25, 15])
        self.mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
        self.mycolors = ["black", "hotpink", "b", "#4CAF50"]

    def plot(self):
        plt.pie(self.y, labels = self.mylabels, colors = self.mycolors)
        plt.show() 

# 創建 PieColor 物件
pie_color = PieColor()
# 呼叫 plot() 方法來繪製圖形
pie_color.plot()


# Add a list of explanation for each wedge
class PieLegend:
    def __init__(self):
        self.y = np.array([35, 25, 25, 15])
        self.mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

    def plot_legend(self):
        plt.pie(self.y, labels = self.mylabels)
        plt.legend()
        plt.show()

    def plot_legend_header(self):
        plt.pie(self.y, labels = self.mylabels)
        plt.legend(title = "Four Fruits:")
        plt.show()

# 創建 PieLegend 物件
pie_legend = PieLegend()
# 呼叫 plot_legend() 方法來繪製圖形
pie_legend.plot_legend()
# 呼叫 plot_legend_header() 方法來繪製圖形
pie_legend.plot_legend_header()

# Extracurricular: Doughnut
class PieDoughnut:
    def __init__(self):
        self.y = np.array([35, 25, 25, 15])
        self.mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
        self.wedgeprops = {'width': 0.4}

    def plot(self):
        plt.pie(self.y, labels=self.mylabels, wedgeprops=self.wedgeprops)
        plt.title("Doughnut Chart")
        plt.show()

# 創建 PieDoughnut 物件
pie_doughnut = PieDoughnut()
# 呼叫 plot() 方法來繪製圖形
pie_doughnut.plot()
