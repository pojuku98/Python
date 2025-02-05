# 質數判定：使用者輸入任意自然數a，將2~a之間所有質數輸出

def is_prime(n):
    for i in range(2, n):                   #從 2 ~ n-1 之間，
        if n % i == 0:                      #若有 i 能整除 n ，
            return False                    #則 n 非質數
    return True                             #無條件滿足則為質數
a = int(input('Input a number: '))
for i in range(2, a+1):                     #將 2 ~ a 所有自然數
    i_is_prime = is_prime(i)                #逐一送入判斷
    if i_is_prime:                          #若回傳為真，
        print(i, end = ' ')                 #則印出