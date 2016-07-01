## 描述:

给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个非连续子序列，使其和最大，输出最大子序列的和。
这里非连续子序列的定义是，子序列中任意相邻的两个数在原序列里都不相邻。
例如，对于L=[2,-3,3,50]， 输出52（分析：很明显，该列表最大非连续子序列为[2,50]).

## solve
```Python
#个人的思路是依旧利用动态规划，状态方程为：
#b[j] = max(b[j - 2] + List[j], b[j - 1], List[j])

def solve(List):
    L = List.copy()
    if len(List) > 1:
        L[1] = max(List[0], List[1])
    for i in range(2, len(List)):
        L[i] = max(L[i - 2] + List[i], L[i - 1], List[i])

    return L[-1]

if __name__ == '__main__':
    L = [8, -3, 2, -3, 3, 60, -100, 50]
    print(solve(L))

"""
看下题解报告的：
---version 1---
n = len(L)
f = list(L)
for i in range(n):
    if i > 0:
        f[i] = max(f[i],f[i-1])
    if i > 1:
        f[i] = max(f[i],f[i-2]+L[i])

print(f[n-1])

其中f[i]表示0-i的最大非连续子序列和

---version 2---
for i in range(2, len(L)):
    L[i] = max(max(L[0:i-1]), 0) + L[i]
print max(L)
"""
```