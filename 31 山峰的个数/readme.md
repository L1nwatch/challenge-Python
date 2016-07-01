## 描述

十一假期,小P出去爬山,爬山的过程中每隔10米他都会记录当前点的海拔高度(以一个浮点数表示),
这些值序列保存在一个由浮点数组成的列表h中。回到家中，小P想研究一下自己经过了几个山峰，请你帮他计算一下，输出结果。
例如：h=[0.9,1.2,1.22,1.1,1.6,0.99], 将这些高度顺序连线，会发现有两个山峰，故输出一个2(序列两端不算山峰)

## solve
```Python
#自己的思路是，遍历一遍，看每个数（除第一个和最后一个以外）是否比两边的数都大
#是的话即为山峰

def countNumOfPeaks(List):
    counts = 0
    for i in range(1, len(List) - 1):
        if List[i] > List[i - 1] and List[i] > List[i + 1]:
            counts += 1

    return counts

if __name__ == '__main__':
    h = [0.9, 1.2, 1.22, 1.1, 1.6, 0.99]
    print(countNumOfPeaks(h))
```