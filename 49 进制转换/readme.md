## 描述

给你一个十进制数a，将它转换成b进制数,如果b>10,用大写字母表示（10用A表示，等等）
a为32位整数，2 <= b <= 16
如a=3,b = 2, 则输出11

## solve
```Python
#基本思路是除b取余法
#搞了半天错误的原因是没处理负数情况，醉了。。。

def solve(num, n):
    character = "0123456789ABCDEF"
    answer = ""
    if num < 0:
        symbol = "-"
        num = -num
    else:
        symbol = ""
    while num > 0:
        answer += character[num % n]
        num //= n

    return symbol + answer[::-1]

if __name__ == "__main__":
    a, b = -100, 16
    print(solve(a, b))

"""
题解：
---version 1---
d = '0123456789ABCEDFGHIJKLMNOPQRSTUVWXYZ'
def f(x,y):
    s = []
    while x>=y:
        s.append(x%y)
        x /=y
    s.append(x)
    return ''.join([d[c] for c in s[::-1]])

print (a<0 and '-' or '')+f(abs(a),b)
"""
```