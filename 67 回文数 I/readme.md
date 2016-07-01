## 描述

若一个数（首位不为0）从左到右读与从右到左读都是一样，这个数就叫做回文数，例如12521就是一个回文数。
给定一个正整数，把它的每一个位上的数字倒过来排列组成一个新数，然后与原数相加，如果是回文数则停止，如果不是，则重复这个操作，直到和为回文数为止。给定的数本身不为回文数。
例如：87则有：
STEP1: 87+78=165
STEP2: 165+561=726
STEP3: 726+627=1353
STEP4: 1353+3531=4884
现在给你一个正整数M（12 <= M <= 100),输出最少经过几步可以得到回文数。如果在8步以内（含8步）不可能得到回文数，则输出0。
例如：M=87，则输出4.

## solve
```Python
#感觉是遍历一遍就出来了

def countTimes(num):
    counts = 0
    while counts <= 8:
        counts += 1
        num = int(str(num)[::-1]) + num
        if isHuiWen(num):
            return counts
    else:
        return 0

def isHuiWen(num):
    return str(num)[::-1] == str(num)

if __name__ == "__main__":
    num = 87
    print(countTimes(num))

"""
题解
---version 1---
flag = 0
for i in range(8):
    M = M + int(str(M)[::-1])
    if str(M) == str(M)[::-1]:
        flag = i + 1
        break
print flag
---version 2---
fg=0
while fg<8:
    S=int(str(M)[::-1])
    D=S+M
    fg += 1
    if D==int(str(D)[::-1]):
        print fg
        break
    else:
        M=D
else:
    print 0
"""
```