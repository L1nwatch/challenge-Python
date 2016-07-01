## 描述

有一组砝码，重量互不相等，分别为m1、m2、m3……mn；它们可取的最大数量分别为x1、x2、x3……xn。
现要用这些砝码去称物体的重量,问能称出多少种不同的重量。
现在给你两个正整数列表w和n， 列表w中的第i个元素w[i]表示第i个砝码的重量，列表n的第
i个元素n[i]表示砝码i的最大数量。i从0开始，请你输出不同重量的种数。
如：w=[1,2], n=[2,1], 则输出5（分析：共有五种重量：0,1,2,3,4）

## solve
```Python
#为啥我看到这种问题，第一眼想到的是背包问题。
#不浪费时间，果断看题解

#喵了一遍题解，DP+遍历的说？
#自己的思路有三种循环。
#一次性过了，简述一下思路吧，第一个循环表示每一个砝码来一次，第二个循环表示
#该砝码从1个取到n[i]个，第三个循环表示上一个的所有情况每个都取一下然后再来+现在的这个

#感觉自己的代码时间复杂度很长，不是一般的长！

def solve(w, n):
    total = set()
    total.add(0)
    length = len(w)
    for i in range(length):
        tmp_set = set()
        for j in range(1, n[i] + 1):
            for each in total:
                tmp = each + j * w[i]
#                print("i = {0}, j = {1}, each = {2}, tmp = {3}"\
#                      .format(i, j, each, tmp))
                if tmp not in total:
                    tmp_set.add(tmp)
        total.update(tmp_set)

    return total

if __name__ == '__main__':
    w = [1, 2]
    n = [2, 1]
    print(len(solve(w, n)))

"""
题解的：
---version 1---
total_w=0
length_n=len(w)
for i in range(length_n):
    total_w+=w[i]*n[i]
S=set([])
S.add(total_w)
for i in range(length_n):
    temp_S=S.copy()
    for s in temp_S:
        j=1
        while j<=n[i]:
            S.add(s-j*w[i])
            j+=1
print len(S)

---version 2---
若m1能被称出，则total_w-m1亦能被称出，如此，可以稍作优化：

total_w=0
length_n=len(w)
for i in range(length_n):
    total_w+=w[i]*n[i]
S=set([])
S.add(total_w)
for i in range(length_n):
    temp_S=S.copy()
    for s in temp_S:
        j=1
        while j<=n[i]:
            if s-j*w[i]>=total_w/2:
                S.add(s-j*w[i])
                S.add(total_w-s+j*w[i])
                j+=1
            else:
                break
print S
print len(S)
"""
```