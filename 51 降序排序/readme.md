## 描述

给你一个list L, 如 L=[2,8,3,50], 对L进行降序排序并输出,
如样例L的结果为[50,8,3,2]

## solve
```Python
if __name__ == "__main__":
    L = [2,8,3,50]
    L.sort(reverse = True)
    print(L)
```