## 描述

给你一个字符串列表L，请用一行代码将列表所有元素拼接成一个字符串并输出。
如L=['abc','d','efg'], 则输出abcdefg。

## solve
```Python
#题目要求一行代码，吓~~~

L=['abc','d','efg']
print(''.join([str(i) for i in L])) #这句好了，在2.X版本下
#题解更简单：
print(''.join(L))



#下面这句在python3.X版本倒是对了，2.X自己报语法错误了
[print(i, end = "") for i in L]
```