import matplotlib.pyplot as plt
import numpy as np

# Focus on variety of marker.
class FocusMarker:
    def __init__(self):
        self.y = np.array([3, 8, 1, 10])
        
    def circle_marker_plot(self):
        """ 圓點Marker """
        plt.plot(self.y, marker = 'o')
        plt.show()

    def star_marker_plot(self):
        """ 星形Marker """
        plt.plot(self.y, marker = '*')
        plt.show()

# 創建 FocusMarker 物件
plot_with_marker = FocusMarker()
# 呼叫 circle_marker_plot() 方法來繪製圖形
plot_with_marker.circle_marker_plot()
# 呼叫 star_marker_plot() 方法來繪製圖形
plot_with_marker.star_marker_plot()

# Practice to use the 'fmt'
class PlotWithFMT:
    def __init__(self):
        self.y = np.array([3, 8, 1, 10])

    def plot_odr(self):
        """ 圓點、虛線、紅色 """
        plt.plot(self.y, 'o:r')
        plt.show()

# 創建 PlotWithFMT 物件
plot_with_fmt = PlotWithFMT()
# 呼叫 plot_odr() 方法來繪製圖形
plot_with_fmt.plot_odr()

# Focus on marker size
class MarkerSize:
    def __init__(self):
        self.y = np.array([3, 8, 1, 10])
        self.marker = 'o'
        pass

    def plot(self):
        plt.plot(self.y, marker = self.marker, ms = 20)
        plt.show()

# 創建 MarkerSize 物件
marker_size = MarkerSize()
# 呼叫 plot() 方法來繪製圖形
marker_size.plot()

# Focus on marker edge color
class MarkerEdgeColor:
    def __init__(self):
        self.y = np.array([3, 8, 1, 10])
        self.marker = 'o'
        self.ms = 20

    def plot(self):
        plt.plot(self.y, marker = self.marker, ms = self.ms, mec = 'r')
        plt.show()

# 創建 MarkerEdgeColor 物件
marker_edge_color = MarkerEdgeColor()
# 呼叫 plot() 方法來繪製圖形
marker_edge_color.plot()

# Focus on marker face color
class MarkerFaceColor:
    def __init__(self):
        self.y = np.array([3, 8, 1, 10])
        self.marker = 'o'
        self.ms = 20

    def plot(self):
        plt.plot(self.y, marker = self.marker, ms = self.ms, mfc = 'r')
        plt.show()

# 創建 MarkerFaceColor 物件
marker_face_color = MarkerFaceColor()
# 呼叫 plot() 方法來繪製圖形
marker_face_color.plot()

# Use both mec & mfc
class MarkerEdgeFaceColor:
    def __init__(self):
        self.y = np.array([3, 8, 1, 10])
        self.marker = 'o'
        self.ms = 20

    def plot_color_short(self):
        plt.plot(self.y, marker = self.marker, ms = self.ms, 
                 mec = 'r', mfc = 'r')
        plt.show()

    def plot_color_hex(self):
        plt.plot(self.y, marker = self.marker, ms = self.ms, 
                 mec = '#4CAF50', mfc = '#4CAF50')  
        plt.show()  

    def plot_color_name(self):
        plt.plot(self.y, marker = self.marker, ms = self.ms, 
                 mec = 'hotpink', mfc = 'hotpink')
        plt.show()


# 創建 MarkerEdgeFaceColor 物件
marker_edge_face_color = MarkerEdgeFaceColor()
# 呼叫 plot_color_short() 方法來繪製圖形
marker_edge_face_color.plot_color_short()
# 呼叫 plot_color_hex() 方法來繪製圖形
marker_edge_face_color.plot_color_hex()
# 呼叫 plot_color_name() 方法來繪製圖形
marker_edge_face_color.plot_color_name()



