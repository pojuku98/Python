import numpy as np
import matplotlib.pyplot as plt

# Example for add title and label
class FocusTitleLabel:
    def __init__(self):
        self.x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
        self.y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

    def plot(self):
        plt.plot(self.x, self.y)

        plt.title("Sports Watch Data")
        plt.xlabel("Average Pulse")
        plt.ylabel("Calorie Burnage")

        plt.show()

# 創建 FocusTitleLabel 物件
example_title_label = FocusTitleLabel()
# 呼叫 plot() 方法來繪製圖形
example_title_label.plot()

# Use fontdict to set font properties
class FontProperty:
    def __init__(self):
        self.x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
        self.y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

        self.font_1 = {'family':'serif','color':'blue','size':20}
        self.font_2 = {'family':'serif','color':'darkred','size':15}

    def plot(self):
        plt.title("Sports Watch Data", fontdict = self.font_1)
        plt.xlabel("Average Pulse", fontdict = self.font_2)
        plt.ylabel("Calorie Burnage", fontdict = self.font_2)

        plt.plot(self.x, self.y)
        plt.show()

# 創建 FontProperty 物件
font_dict = FontProperty()
# 呼叫 plot() 方法來繪製圖形
font_dict.plot()

# Use the loc in title() to position the title.
class TitlePosition:
    def __init__(self):
        self.x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
        self.y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

        self.title = "Sports Watch Data"
        self.xlabel = "Average Pulse"
        self.ylabel = "Calorie Burnage"

    def plot(self):
        plt.title(self.title, loc = 'left')
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        plt.plot(self.x, self.y)
        plt.show()

# 創建 TitlePosition 物件
loc_title = TitlePosition()
# 呼叫 plot() 方法來繪製圖形
loc_title.plot()


