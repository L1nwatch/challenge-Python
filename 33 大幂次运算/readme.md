## 描述:

给你两个正整数a(0 < a < 100000)和n(0 <= n <=100000000000)，计算(a^n) % 20132013并输出结果

## solve
```Python
def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e&1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b*b) % m
    return result

a, n = 5, 6
print(fastExpMod(a, n, 20132013))
```

***

    ======================上面也是快速幂取模，跑起来对的！！！=========================

```Python
#之前ACM有做过，就是求模公式呗
"""
翻一下acm笔记：
(a * a) % m = ( a % m * a % m ) % m
"""

#看了下题解，说是快速幂（之前ACM刷斐波那契的时候应该遇到过了，就是二分矩阵快速求幂）
#直接看题解报告了，自己写出算法是不太可能的。。。
#题解。。。。牛过头了：print(pow(a, n, 20132013))

"""
以下说是快速幂取模：
a^b mod c = ((a^2)^(b / 2)) mod c, b是偶数
a^b mod c = ((a^2)^(b / 2) * a) mod c, b是奇数

#下面的代码，在自己的机子上跑着是错的，但是在网上跑的确是对的？python版本的问题我估计！
def PowerMod(a, n, ret):
    if n == 0:
        return ret
    if n % 2:
        ret = ret * a % 20132013

    return PowerMod( a * a % 20132013, n / 2, ret)

if __name__ == '__main__':
    a, n = 5, 6
    ret = 1
    print(PowerMod(a, n, ret))
"""

"""
version 1
说是算法超时了...
O(n)算法说我超时了，好吧，看来只能看题解了
def solve(a, n):
    result = 0
    if n == 0:
        result = 1
    else:
        result = a % 20132013
        n -= 1

    while n > 0:
        n -= 1
        result = (result * (a % 20132013)) % 20132013

    return result

if __name__ == '__main__':
    a, n = 5, 5
    print(solve(a, n))
"""
```