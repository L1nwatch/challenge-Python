## 描述:

给你一个正整数列表 L, 如 L=[2,8,3,50], 判断列表内所有数字乘积的最后一个非零数字的奇偶性,
奇数输出1,偶数输出0. 如样例输出应为0

## solve
```Python
#看了题解:分析所有数字的约数中2和5的数量，总有如果n(2)>n(5)，则结果必为偶数

def solve( L ) :
    num_2 = 0
    num_5 = 0
    for each in L :
        num_5 += count_mod( each,5 )
        num_2 += count_mod( each,2 )
    return 1 if num_2 <= num_5 else 0

def count_mod( number,mod ) :
    counts = 0
    while number % mod == 0 :
        counts += 1
        number /= mod
    return counts

if __name__ == '__main__' :
    L = [ 1,2,3,4,5 ]
    L = [ 2,8,10 ]
    L = [ 5,8,1000 ]
    L = [ 5,8,1 ]
    print( solve( L ) )
```