## 描述

有一楼梯共n级，刚开始时你在第一级，若每次只能跨上一级或二级，要走上第n级，共有多少种走法？
现在给你一个正整数n（0<n<40),请你输出不同的走法数。
如n=2,则输出1（你只有一种走法，走一步，从第一级到第二级）

## solve
```Python
#这道题不就是斐波那契么，= =我觉得是
#f[n] = f[n - 1] + f[n - 2]
#因为n比较少，所以我用迭代吧

"""
另一种迭代的表达形式：
a = 1
b = 2
for i in range(1, n-1):
    c = a + b
    a = b
    b = c
print a
"""

def fibonacci(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])

    return f[-1]

if __name__ == '__main__':
    n = 4
    print(fibonacci(n))
```