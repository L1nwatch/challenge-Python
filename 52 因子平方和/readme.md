## 描述

6 的因子有 1, 2, 3 和 6, 它们的平方和是 1 + 4 + 9 + 36 = 50. 如果 f(N) 代表正整数 N 所有因子的平方和, 那么 f(6) = 50.
现在令 F 代表 f 的求和函数, 亦即 F(N) = f(1) + f(2) + .. + f(N), 显然 F 一开始的 6 个值是: 1, 6, 16, 37, 63 和 113.
那么对于任意给定的整数 N (1 <= N <= 10^8), 输出 F(N) 的值.

## solve
```Python
#目测自己的算法会超时
#思路：一个函数用于求因子，一个函数用于求因子的和f(N)，一个函数用于求F(N)
#果然超时了。

"""
附题解2个，自己还没解决出来：
---version 1---


这道题直接做回超时。

技巧一：F(N)可以看作N个1*＊2，N/2个2*＊2，N/3个3＊＊2，，，，，以此类推。即便这样，还会超时。

技巧二：对称。N个1*＊2对称1个N**2，N/2个2*＊2对称2个N/2**2,,,,,,. 但是，值得注意的是对称并不是一对一的，而是一对多的。比如N个1*＊2对称的是1个 (N/2**2,,,,,,,(N-1)**2，N**2］。依次类推。

import math
def sumsqr(m, n):
    if m >= n:
        return 0
    return n*(n+1)*(2*n+1)/6-m*(m+1)*(2*m+1)/6
def F(n):
    i=1
    seg=[]
    sum1=0
    high = n;
    while i*i <=n:
        sum1 += (n/i)*i**2
        low = max(n/(i+1), i);
        sum1 += i*sumsqr(low,high)
        i += 1
        high = low
    return sum1

F(N)
计算清楚每个N**2序列的个数即可

def func(N):
    result=0
    n=N+1
    a,b=0,0
    while n>1:
        n=N/(N/n+1)
        a,b=N/n,a
        print n
        result+=(a-b)*n*(n+1)*(2*n+1)/6
print func(N)
sorry，贴错了~更新下：

def func(N):
    result=0
    n=N+1
    a,b=0,0
    while n>1:
        n=N/(N/n+1)
        a,b=N/n,a
        result+=(a-b)*n*(n+1)*(2*n+1)/6
    return result
print func(N)

---version 2---
#N = 2

def cal(x):
    return x * (x + 1) * (2 * x + 1) / 6

ans = 0

for i in range(1, N / 10 + 1):
    ans += (N / i) * i * i
for i in range(9, 0, -1):
    ans += i * (cal(N / i) - cal(N / (i + 1)))
print ans


"""

def getDivisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors

def getDivisorsSum(num):
    divisors = getDivisors(num)
    answer = 0
    for each in divisors:
        answer += each ** 2

    return answer

def getTotalDivisorsSum(num):
    answer = 0
    for i in range(num):
        answer += getDivisorsSum(i + 1)

    return answer

if __name__ == "__main__":
    for N in range(1, 8):
        print(getTotalDivisorsSum(N))
```