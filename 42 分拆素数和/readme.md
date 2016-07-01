## 描述

把一个偶数拆成两个不同素数的和，有几种拆法呢？
现在来考虑考虑这个问题，给你一个不超过10000的正的偶数n，
计算将该数拆成两个不同的素数之和的方法数，并输出。
如n=10，可以拆成3+7，只有这一种方法，因此输出1.

## solve
```Python
#个人思路，遍历一遍10000以内的素数。
#然后我就得先有个10000以内的素数表

#自己的方法虽然过了，但是个人觉得时间复杂度应该会高些，毕竟是O(n)算法
"""
以下看下题解吧：
看了题解，比较喜欢的是这个(利用哈希表而不是列表这样时间复杂度快了N多)：
def sushuDic(n):
dic = {x: True for x in range(2, n)}
for x in dic.keys():
if dic[x]:
i = x * 2
while i < n:
dic[i] = False
i = i + x
return dic


def divideCnt(n):
dic = sushuDic(n)
cnt = 0
for i in range(2, n // 2):
if dic[i] and dic[n-i]:
cnt = cnt + 1
return cnt

print divideCnt(n)

用哈希表快速求素数。
"""
import  math

def createPrimeList(num):
    List = []

    for i in range(2, num):
        prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            List.append(i)

    return List

def countWays(num, prime_list):
    counts = 0
    for each in prime_list:
        if each >= num:
            break
        elif each != (num - each) and (num - each) in prime_list:
            counts += 1

    return counts // 2

if __name__ == '__main__':
    prime_list = createPrimeList(10000)
    n = 10
    ways = countWays(n, prime_list)
    print(ways)
```