# Pandas 是 Python 的數據處理庫，提供強大的 DataFrame 和 Series 結構，
# 便於高效的數據清理、操作與分析，廣泛應用於數據科學與工程。

# 2-4-1
import pandas as pd

import numpy as np

# 2-4-2
# pd.Series：類似一維陣列的物件。說起來Pandas的基礎就是Numpy的array
data_series = pd.Series([0,10,20,30,40,50,60,70,80,90])
print(f"Series -- 一維陣列：\n{data_series}")

# 將series的索引( index )設定為英文字母
data_series_indexed = pd.Series(
    [0,10,20,30,40,50,60,70,80,90],
    index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(f"一維陣列，手動設定索引：\n{data_series_indexed}")

# .values：取得series的值
# .index ：取得series的索引
print(f"一維陣列的資料：{data_series_indexed.values}")
print(f"一維陣列的索引：{data_series_indexed.index}")

# 2-4-3
# 製作DataFrame前置作業：先以dict型別寫入資料
# 可由：print(type(attri_data1))，確認此變數型別為dict
data_dictionary_1 = {'ID':['100','101','102','103','104'], 
                     'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'], 
                     'Birth_year':[1990,1989,1992,1997,1982], 
                     'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}
# 將dict型別的資料轉為DataFrame
# pd.DataFrame：二維陣列，對於各行，也能設定不同dtype(資料型別)
data_DataFrame_1 = pd.DataFrame(data_dictionary_1)
print(f"DataFrame -- 二維陣列：\n{data_DataFrame_1}")

# 將DataFrame的索引( index )設定為英文字母
data_DataFrame_1_indexed = pd.DataFrame(data_dictionary_1, index=['a','b','c','d','e'])
print(f"二維陣列，手動設定索引：\n{data_DataFrame_1_indexed}")

# 2-4-4-1
# .T：矩陣的轉置
data_DataFrame_1_trans = data_DataFrame_1.T
print(f"將矩陣轉置：\n{data_DataFrame_1_trans}")

# 2-4-4-2
# 取出特定行
# 指定行名(1個的情況)
print(f"取出特定 一行：\n{data_DataFrame_1.Birth_year}")
# 指定行名(多個的情況)，一個[]代表索引、一個[]代表裝成list
print(f"取出特定 多行：\n{data_DataFrame_1[['ID', 'Birth_year']]}")

# 2-4-5
# 依條件抽取資料
# 條件( 過濾器 )
print(f"一個條件：\n{data_DataFrame_1[data_DataFrame_1['City'] == 'Tokyo']}")
# 條件部份的表示式，是將City行的元素逐一與Tokyo比較
print(f"其中，條件式會以布林值計算：\n{data_DataFrame_1['City'] == 'Tokyo'}")
# 條件( 過濾器、多個值 使用.isin(list) )
print(f"多個條件：\n{data_DataFrame_1[data_DataFrame_1['City'].isin(['Tokyo','Osaka'])]}")

# 2-4-6-1
# .drop()：刪除特定的行或列。參數axis指定軸，axis=0為列、axis=1為行
# 好險不會直接改到原本矩陣
data_DataFrame_1_drop = data_DataFrame_1.drop(['Birth_year'], axis=1)
print(f"刪除Birth_year那行：\n{data_DataFrame_1_drop}")
print(f"原本的第一矩陣：\n{data_DataFrame_1}")

# 2-4-6-2
# 準備第二個矩陣
data_dictionary_2 = {'ID':['100','101','102','105','107'], 
                     'Math':[50,43,33,76,98], 
                     'English':[90,30,20,50,30], 
                     'Sex':['M','F','F','M','M']}
data_DataFrame_2 = pd.DataFrame(data_dictionary_2)
print(f"DataFrame -- 第二個二維陣列：\n{data_DataFrame_2}")

# 資料合併(內部結合)
# pd.merge()參數預設為inner join
merge_frame = pd.merge(data_DataFrame_1, data_DataFrame_2)
print(f"兩表內部結合：\n{merge_frame}")

# 2-4-7
# 資料的群組別統計
# 以('Sex')欄位分群，計算各別['Math']的平均：.mean()
data_DataFrame_2_group = data_DataFrame_2.groupby('Sex')['Math'].mean()
print(f"分群統計：\n{data_DataFrame_2_group}")

# 2-4-8
# 準備第三個矩陣
data_dictionary_3 = {'ID':['100','101','102','103','104'],
                     'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
                     'Birth_year':[1990,1989,1992,1997,1982],
                     'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}
data_DataFrame_3 = pd.DataFrame(data_dictionary_3)
data_DataFrame_3_indexed = pd.DataFrame(data_dictionary_3, index=['e','b','a','d','c'])
print(f"DataFrame -- 第三個二維陣列，手動變更索引：\n{data_DataFrame_3_indexed}")

# .sort_index()：基於index的排序
print(f"以 索引排序：\n{data_DataFrame_3_indexed.sort_index()}")

# .sort_values()：要先指定欄位，基於 值 的排序，預設由小到大
print(f"以 值排序：\n{data_DataFrame_3_indexed.Birth_year.sort_values()}")

# 2-4-9-2
# nan與null的例子
# .copy()：創建副本。避免直接修改原始資料
# np.nan：將指定資料設定為nan
# .isnull()：判斷是否為nan
data_DataFrame_3_indexed_nan = data_DataFrame_3_indexed.copy()
data_DataFrame_3_indexed_nan['Name'] = np.nan
print(f"判斷為nan的資料：\n{data_DataFrame_3_indexed_nan.isnull()}")
print(f"原本的改索引第三矩陣：\n{data_DataFrame_3_indexed}")

# 統計各欄位資料中出現null(nan)的總數
print(f"每個欄位有多少null值：\n{data_DataFrame_3_indexed_nan.isnull().sum()}")