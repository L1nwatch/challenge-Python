## 描述:

还记得中学时候学过的杨辉三角吗？具体的定义这里不再描述，你可以参考以下的图形：
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
..............
先在给你一个正整数n，请你输出杨辉三角的前n层
注意：层数从1开始计数,每层数字之间用一个空格隔开，行尾不要有空格。
如n=2,则输出：
1
1 1

## solve
```Python
#记得自己在ACM写过，不过顿时想不起来了，
#看了ACM之家的题解，发现全都是记录上一层然后求出这一层的，没有其他好方法，那么就这样吧
#以下是看着ACM的C++杨辉三角写的http://www.acmerblog.com/hdu-2032-3119.html

def getNum(row, col, num):
    if col == 0 or col == row:
        num[row][col] = 1
    if num[row][col] == -1:
        num[row][col] = getNum(row - 1, col - 1, num) + \
                        getNum(row - 1, col, num)

    return num[row][col]

def solve(n, num_array):
    for i in range(n):
        for j in range(i):
            print(getNum(i, j, num_array), end = ' ')#2.X版本:print(getNum(i, j, num_array)),
        print(getNum(i, i, num_array), end = '\n')#2.X版本print(getNum(i, i, num_array))

def createNumArray(n):
    num = []
    for i in range(n):
        num.append([-1 for i in range(n)])

    return num

if __name__ == "__main__":
    for n in range(1, 20):
        num_array = createNumArray(n)
        solve(n, num_array)
```