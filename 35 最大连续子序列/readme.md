## 描述:

给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个连续子序列，使其和最大，输出最大子序列的和。
例如，对于L=[2,-3,3,50]， 输出53（分析：很明显，该列表最大连续子序列为[3,50]).

## solve
```Python
#ACM老师讲过的一道题（比这难得多的），PPT里有，动态规划
#查看了一下课件，得到状态方程：b[j]=max( b[j-1]+a[j], 0+a[j] ), 1<=j<=n

def getLargestSum(List):
    b = 0
    largest_sum = 0
    for each in List:
        if b > 0:
            b += each
        else:
            b = each
        largest_sum = max(b, largest_sum)

    return largest_sum

if __name__ == '__main__':
    List = [2, -3, 3, 50]
    print(getLargestSum(List))
```