import matplotlib.pyplot as plt
import numpy as np

# Example of basic histogram
class ExampleHistogram:
    def __init__(self):
        self.x = np.random.normal(170, 10, 250)

    def plot(self):
        plt.hist(self.x)
        plt.show() 

# 創建 ExampleHistogram 物件
example_hist = ExampleHistogram()
# 呼叫 plot() 方法來繪製圖形
example_hist.plot()


