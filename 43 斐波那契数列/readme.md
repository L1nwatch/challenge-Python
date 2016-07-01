## 描述

斐波那契数列为1,1,2,3,5,8...。数列从第三项起满足，该项的数是其前面两个数之和。
现在给你一个正整数n（n < 10000), 请你求出第n个斐波那契数取模20132013的值（斐波那契数列的编号从1开始）。

## solve
```Python
#这道题我还是搬ACM的题解吧，毕竟之前用那个方法（C++下的）过了2ms的题
#所以算法时间复杂度绝对是可以的

#以下：f[n] = f[n - 1] + f[n - 2]
#附算法网址：http://www.acmerblog.com/fibonacci-3395.html

"""
题解用的迭代：
def count(n):
    x = [0,1]
    for i in range(2,n+1):
        x.append(x[i-1] + x[i-2])
    return x[n]

print count(n)%20132013
"""

def multiply(c, a, b, mod):
    tmp = [ a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1] ]
    c[0][0] = tmp[0] % mod
    c[0][1] = tmp[1] % mod
    c[1][0] = tmp[2] % mod
    c[1][1] = tmp[3] % mod

def fibonacci(n, mod):
    if n == 0:
        return 0
    elif n <= 2:#这里表示第0项为0，第1，2项为1
        return 1

    a = [[1, 1], [1, 0]]
    result = [[1, 0], [0, 1]]
    n -= 2
    while n > 0:
        if n % 2 == 1:
            multiply(result, result, a, mod)
        multiply(a, a, a, mod)
        n //= 2 #注意这里不能写n /= 2,得用地板除法

    s = (result[0][0] + result[0][1]) % mod
    return s

if __name__ == '__main__':
    mod = 20132013
    answer = fibonacci(n, mod)
    print(answer)
```