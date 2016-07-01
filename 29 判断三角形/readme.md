## 描述

给你三个整数a,b,c,  判断能否以它们为三个边长构成三角形。
若能，输出YES，否则输出NO。

## solve
```Python
#三角形两边之和大于第三边，两边之差小于第三边
#一次性AC

"""
关于判定定理的问题，这里有两种说法：

legend_001 评论于 2014-07-12 11:33:30
先sort，然后保证前两个的和大于第三个就好，因为sort之后就保证了前两个的差小于第三个
ylgkger 评论于 2014-12-19 19:10:27
简化 a+b+c-max(a,b,c)*2>0即可
"""

def canBeTriangle(a, b, c):
    List = [a, b, c]
    List.sort()
    return (List[0] + List[1] > List[2]) and (List[2] - List[0] < List[1])

if __name__ == '__main__':
    a, b, c = 3, 4, 5
    if canBeTriangle(a, b, c):
        print("YES")
    else:
        print("NO")
```