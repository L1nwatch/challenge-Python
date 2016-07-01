## 描述

给你直角三角形的两个直角边的边长a,b,请你求出其斜边边长，结果保留小数点后三位小数。
如a=3, b =4, 则输出5.000。

## solve
#勾股定理的公式不就是c^2 = a^2 + b^2么
#print '%.3f' %(a**2+b**2)**0.5

def getC(a, b):
    c = a ** 2 + b ** 2
    return c ** 0.5

if __name__ == '__main__':
    a, b = 3, 4
    answer = getC(a, b)
    print(format(answer, '.3f'))
