## 描述

光棍们对1总是那么敏感，因此每年的11.11被戏称为光棍节。
鄙人光棍几十载，光棍自有光棍的快乐。让我们勇敢面对光棍的身份吧，
现在就证明自己：给你一个整数a，数出a在二进制表示下1的个数，并输出。

## solve
```Python
def solve( num ) :
    return bin( num ).count( "1" )

"""
bin为内置函数，将num转换成二进制数（要求num整数或者包含__index__()方法切返回值为integer的类型）
"""

if __name__ == '__main__' :
    num = 11
    print( solve( num ) )
```