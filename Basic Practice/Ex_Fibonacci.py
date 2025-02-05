# 由使用者輸入指定費氏數列第a個數，將費氏數列從頭到第a個數全部印出

def fib(n):
    if n > 1:                           #大於1之後，
        return fib(n-1) + fib(n-2)      #利用遞迴，回頭找頭二項
    else:                               #頭二項：fib(0), fib(1)
        return n                        #直接以引數值回傳
    
a = int(input('Input a number: '))
for i in range(a):
    if i == a-1:
        print(fib(i))
    else:
        print(fib(i), end = ',')