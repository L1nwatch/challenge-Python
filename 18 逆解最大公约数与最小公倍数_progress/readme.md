## 描述

我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。
今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。
注：所给数据都有解，不用考虑无解的情况。

## solve
```Python
#最小公倍数=俩数之积/最大公约数
#个人思路：最大公约数*最小公倍数，即得两数之积，遍历一下?
#网上的思路，看着不错
"""
思路：a/gcd * b/gcd = lcm/gcd
还有一个常识性质的性质：a*b为定值时，a和b相差越小，a+b越小
所以从lcm/gcd的平方根开始枚举a即可。
"""

"""
PS:注意算法算出来之后还得乘上gcd才对啊!!!!!!
"""
import math

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

def lcm(x, y):
    return x * y / gcd(x, y)

def getTheTwoNum(num_gcd, num_lcm):
    List = []
    tmp = num_lcm / num_gcd
    for a in range(int(math.sqrt(tmp)), 0, -1):
        if tmp % a == 0:
            b = tmp / a
            if gcd(a, b) == 1:
                List.append(a * num_gcd)
                List.append(b * num_gcd)
                break

    return List

if __name__ == '__main__':
    num_gcd = 4
    num_lcm = 16
    List = getTheTwoNum(num_gcd, num_lcm)
    List.sort()
    print("%d %d" % (List[0], List[1]))
```