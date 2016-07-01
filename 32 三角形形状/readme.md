## 描述:

给以一个三角形的三边长a,b和c(边长是浮点数),请你判断三角形的形状。
若是锐角三角形，输出R,
若是直角三角形，输出Z，
若是钝角三角形，输出D，
若三边长不能构成三角形，输出W.

## solve
```Python
#自己想到的思路是用余弦定理
#baidu了一下，发现是用最大边所对应的角来计算
"""
若最大边的平方等于另两边的平方和,则它为直角三角形;
若最大边的平方大于另两边的平方和,则它为钝角三角形;
若最大边的平方小于另两边的平方和,则它为锐角三角形.
"""

def canBeTriangle(a, b, c):
    List = [a, b, c]
    List.sort()
    if (List[0] + List[1] > List[2]) and (List[2] - List[0] < List[1]):
        return True
    else:
        return False

def getTypeOfTriangle(a, b, c):
    List = [i ** 2 for i in [a, b, c]]
    List.sort()
    result = List[2] - List[1] - List[0]
    if result == 0:
        return "Z"
    elif result < 0:
        return "R"
    elif result > 0:
        return "D"

if __name__ == '__main__':
    a, b, c = 3, 4, 5
    if canBeTriangle(a, b, c) == False:
        print("W")
    else:
        print(getTypeOfTriangle(a, b, c))
```