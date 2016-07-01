## 描述

给你一个整数列表L,判断L中是否存在相同的数字，
若存在，输出YES，否则输出NO。

## solve
```Python
#一上来两个思路，一个是转换成set集合再比较长度，另一个是遍历一遍

def hasSameNum(List):
    return len(set(List)) != len(List)

if __name__ == '__main__':
    L = [1, 2, 3]
    if hasSameNum(L):
        print("YES")
    else:
        print("NO")
```