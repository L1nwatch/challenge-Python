## 描述

给你两个正整数a,b,  输出它们公约数的个数。

## solve
```Python
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

def countGCD(x, y, max_gcd):
    counts = 1
    for i in range(2, max_gcd + 1):
        if x % i == 0 and y % i == 0:
            counts += 1

    return counts

if __name__ == '__main__':
    x, y = 11, 55
    max_gcd = gcd(x, y)
    counts = countGCD(x, y, max_gcd)
    print(counts)
```