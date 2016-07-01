## 描述

给你一个正整数列表 L, 如 L=[2,8,3,50], 输出L内所有数字的乘积末尾0的个数,
如样例L的结果为2.(提示:不要直接相乘,数字很多,可能溢出)

## solve
```Python
`#看了题解：总的来说就是计算除以2和除以5的个数，输出最小的就可以了

def solve( L ) :
    num_2 = 0
    num_5 = 0
    for each in L :
        num_5 += count_mod( each,5 )
        num_2 += count_mod( each,2 )
    return num_2 if num_2 <= num_5 else num_5

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
    L = [ 5,8,1 ]   #正整数
    print( solve( L ) )
```