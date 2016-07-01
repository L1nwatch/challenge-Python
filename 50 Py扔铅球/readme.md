## 描述

Py不但是编程大牛，而且是运动健将。比如说扔铅球，1000m，现在Py参加校园扔铅球比赛，
给你Py的身高a（双精度数），球落地点与Py头部的连线与水平线的夹角 b（弧度），
要你编写一个程序计算Py扔铅球的水平距离。
a，b都是浮点数，注意b是弧度，其中， 140 < a < 200,  0 < b < 1.5.
输出你求出的水平距离，保留到小数点后三位。
如，a = 165.5, b=1.1, 则输出84.234

## solve
```Python
#思路：画一下图，易得a/x = tanb(θ)
#format函数参考：http://pyformat.info/

import math

def solve(a, b):
    answer = a / math.tan(b)    #注意math.tan(b)本来就要求弧度制而不是角度!
    return answer

if __name__ == "__main__":
    a, b = 165.5, 1.1
    print('{:.3f}'.format(solve(a, b)))
```