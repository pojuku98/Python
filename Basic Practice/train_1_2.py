# 以兩種方式計算1~50之間自然數總和並輸出

# 以for迴圈計算
def sum_with_for(start, end):
    total = 0
    for i in range(start, end+1):
        total += i
    return total

# 以函式計算
def sum_with_function(start, end):
    return sum(range(start, end+1))

start, end = 1, 50

print(f"以 for迴圈計算：{sum_with_for(start, end)}")
print(f"以內建函式計算：{sum_with_function(start, end)}")