## 描述

有两堆石子，数量任意，可以不同。游戏开始由两个人轮流取石子。游戏规定，每次有两种不同的取法，
一是可以在任意的一堆中取走任意多的石子；二是可以在两堆中同时取走相同数量的石子。最后把石子全部取完者为胜者。
现在给出初始的两堆石子的数目a和b，如果轮到你先取，假设双方都采取最好的策略，问最后你是胜者还是败者。
如果你是胜者，输出Win,否则输出Loose。
例如，a=3,b=1, 则输出Win(你先在a中取一个，此时a=2，b=1,此时无论对方怎么取，你都能将所有石子都拿走).

## solve
```Python
#之前在ACM课上听过，这是博弈论的东西
#查了一下，是威佐夫博奕
#ACM解题报告：http://blog.csdn.net/csust_acm/article/details/7957180

import math

def solve(a, b):
    '面对非奇异局势，先拿者必胜；反之，则后拿者取胜。'
    a, b = min(a, b), max(a, b) #奇异局势下，bk > ak
    k = b - a #奇异局势下，bk = ak + k
    m = int((math.sqrt(5.0) + 1) * k / 2) #奇异局势下，ak = 这个公式
    return m != a #若m == a，则为奇异局势，先拿者必败

if __name__ == '__main__':
    a, b = 3, 1
    a, b = 2, 1
    a, b = 8, 4
    a, b = 4, 7
    if solve(a, b):
        print("Win")
    else:
        print("Loose")

"""
题解用到了奇异态势，并不好理解。
相关分析参考：http://blog.renren.com/share/251405117/755224137

推出一个概念：奇异态势。有以下特点：

1.无法从一个奇异态势一步走到另一个奇异态势；

2.任何非奇异态势可以一步走到某一个奇异态势。

于是可构建以下奇异态势，前几组分别为(0,0),(1,2),(3,5),(4,7),(6,10),(8,13)....满足：1）各奇异态势间无重复元素；2）步长（|a-b|）递增，保证各不相同

以此可以计算出(a,b)以下的奇异态势，若(a,b)不在其中，则必赢。

题解代码：
m,n=max(a,b),min(a,b)
small_num=0
large_num=0
step=0
S=set([])
S.add(small_num)
S.add(large_num)
Win=True
while small_num<n and large_num<m:
    while small_num in S:
        small_num+=1
    step+=1
    large_num=small_num+step
    S.add(small_num)
    S.add(large_num)
    if small_num==n and large_num==m:
        Win=False
        break
#    print '('+str(small_num)+','+str(large_num)+')'
if Win:
    print 'Win'
else:
    print 'Loose'
"""
```