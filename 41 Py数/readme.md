## 描述

Py从小喜欢奇特的东西，而且天生对数字特别敏感，一次偶然的机会，他发现了一个有趣的四位数2992，
这个数，它的十进制数表示，其四位数字之和为2+9+9+2=22，它的十六进制数BB0，其四位数字之和也为22，
同时它的十二进制数表示1894，其四位数字之和也为22，啊哈，真是巧啊。
Py非常喜欢这种四位数，由于他的发现，所以这里我们命名其为Py数。
现在给你一个十进制4位数n，你来判断n是不是Py数，若是，则输出Yes，否则输出No。
如n=2992，则输出Yes； n = 9999，则输出No。

## solve
```Python
http://www.68idc.cn/help/jiabenmake/qita/2014042492096.html

#需要用到十二进制，所以得自己写一个10进制转n进制的转换函数
"""
看了下题解，自愧不如啊，果然我傻逼了。。。代码重复性太高了我自己的
def conv(n,m):
    temp = []
    while n != 0:
         temp.append(n % m)
         n = n / m
    return sum(temp)

print conv(n,16) == conv(n,12) == conv(n,10) and 'Yes'or 'No'
"""
def decimal2n(num, n):
    '采用除n取余法'
    answer = ""
    while True:
        answer = str(num % n) + answer
        num = num // n
        if num <= 0:
            break

    return answer

def isPyNum(num):
    dec_sum = sum([int(i) for i in str(num)])
    if isSixteenPyNum(num, dec_sum) and isTwelvePyNum(num, dec_sum):
        return True
    else:
        return False

def isSixteenPyNum(num, total):
    num = hex(num)[2:]
    hex_sum = sum([int(i, 16) for i in str(num)])

    return hex_sum == total

def isTwelvePyNum(num, total):
    num = decimal2n(num, 12)
    twelve_sum = sum([int(i, 12) for i in str(num)])

    return twelve_sum == total

if __name__ == '__main__':
    num = 2992
    if isPyNum(num):
        print("Yes")
    else:
        print("No")
```