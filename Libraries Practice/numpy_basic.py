# NumPy 是 Python 的數值計算庫，提供高效的多維陣列運算
# 和強大的數學、統計、線性代數函式，廣泛應用於科學計算與機器學習。

# 2-2-1
import numpy as np
# 2-2-3
import numpy.random as random

# 2-2-2-1
# 自訂將Numpy陣列四捨五入到小數點後第三位的函示
# np.around()：將Numpy陣列元素四捨五入。參數decimals：指定到小數點後第幾位
def np_array_around_float3(arr):
    arri = np.around(arr, decimals=3)
    return arri

# 製作陣列
data = np.array([9, 2, 3, 4, 10, 6, 7, 8, 1, 5])
print(f"可以在Python使用陣列：{data}")

# 2-2-2-2
# .dtype：查詢Numpy中的資料型別。
print(f"此陣列元素的型別：{data.dtype}")

# 2-2-2-3
# .ndim：取得陣列維度。
# .size：取得陣列元素數量。與Python原生使用len()不同，須注意。
print(f"維度：{data.ndim}，屬於{data.ndim}維陣列")
print(f"元素數量：{data.size}")

# 2-2-2-4
# 原生Python中，要將串列所有元素 *2 ，需使用for迴圈；
# Numpy 只需要直接對陣列物件運算即可
print(f"直接對陣列操作計算：data * 2 = {data * 2}") 

# 2-2-2-5
# .sort：對陣列作排序，預設為升冪；指定陣列切片[::-1]，即可達成降冪
data.sort()
print(f"陣列升冪排序：{data}")
data[::-1].sort()
print(f"陣列降冪排序：{data}")

# 2-2-2-6
print(f"最小值：{data.min()}")
print(f"最大值：{data.max()}")
print(f"總和  ：{data.sum()}")
print(f"累積和：{data.cumsum()}")

data_ratio = data.cumsum() / data.sum()
data_ratio_arounded = np_array_around_float3(data_ratio)
print(f"累積比例：{data_ratio_arounded}")

# 2-2-3-1
# random.seed()：亂數種子。指定相同的種子值，保證每次都能取得相同序列的亂數
random.seed(0)

# 2-2-3-2
# random.randn()：產生常態分布(平均為0、標準差為1)的10個亂數
rnd_data = random.randn(10)
rnd_data_arounded = np_array_around_float3(rnd_data)
print(f"含有10個亂數的陣列：{rnd_data_arounded}")

# 2-2-3-3
# random.choice()：隨機取出
# 取出10個，允許重複，放回抽樣
print(f"從陣列data中，抽樣10個、取後放回：{ random.choice(data, 10) }")
# 取出10個，不允許重複，不放回抽樣
print(f"從陣列data中，抽樣10個、取後不放回：{ random.choice(data, 10, replace=False) }")

# 2-2-4
# 矩陣
# np.arange()：產生指定連續整數
# .reshape()：改變矩陣形狀
matrix_1 = np.arange(9).reshape(3,3)
print(f"1號矩陣：\n{matrix_1}")

# 由切片訪問矩陣內容：[列範圍,行範圍]，各範圍內"開始索引：結束索引"
print(f"1號矩陣的 2列2行：{matrix_1[1][1]}")
print(f"1號矩陣的 3列1、2行：{matrix_1[2:,:2]}")

# 2-2-4-1
# 矩陣運算
matrix_2 = np.arange(9,18).reshape(3,3)
print(f"2號矩陣：\n{matrix_2}")

# np.dot()：就是內積
matrix_dot_function = np.dot(matrix_1, matrix_2)
print(f"1、2號矩陣以 函式 內積：\n{matrix_dot_function}")

# @：矩陣運算子，效果與np.dot()相同
matrix_dot_operator = matrix_1 @ matrix_2
print(f"1、2號矩陣以 運算子 內積：\n{matrix_dot_operator}")

# 2-2-4-2
# np.zeros：產生所有元素均為0的矩陣，參數dtype用於指定資料型別
# np.ones：產生所有元素均為1的矩陣，同上可使用dtype
zero_matrix = np.zeros((2, 3), dtype=np.int64)
print(f"零矩陣：\n{zero_matrix}")
ones_matrix = np.ones((2, 3), dtype=np.float64)
print(f"全一矩陣：\n{ones_matrix}")
