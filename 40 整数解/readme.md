## 描述

给你两个整数a和b（-10000<a,b<10000），请你判断是否存在两个整数，他们的和为a，乘积为b。
若存在，输出Yes,否则输出No
例如：a=9,b=15, 此时不存在两个整数满足上述条件，所以应该输出No。

## solve
```Python
#看到a和b那么小，一下子就想遍历了。。。
#看version 1的遍历，一下子就超时了，说明不行
#x + y = a, x * y = b ==> x * ( a - x ) = b，这样就只有一层遍历了

#看题解居然使用解方程的方法
#题解的时间复杂度为O(1)啊，醉了：
#两个数应该为方程x^2 - a*x + b = 0 的解，判断delta即可

def isExist(a, b):
    for i in range(-9999, 10000):
        if i * ( a - i ) == b:
            return True

    return False

if __name__ == '__main__':
    a, b = 9, 15
    if isExist(a, b):
        print("Yes")
    else:
        print("No")

"""
---version 2---
题解：
from math import sqrt
delta = a*a - 4*b
if delta > 0 and int(sqrt(delta)) == sqrt(delta):
    print "Yes"
else:
    print "No"
"""

"""
---version 1---
def isExist(a, b):
    for i in range(-9999, 10000):
        for j in range(-9999, 10000):
            if i + j == a and i * j == b:
                return True

    return False
"""
```