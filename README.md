# 目录
- [OJ 网址](#oj-网址)  
- [题目 1: just print a+b](#题目-1-just-print-ab)
- [题目 2: list排序](#题目-2-list排序)
- [题目 3: 字符串逆序](#题目-3-字符串逆序)
- [题目 4: 输出字典 key](#题目-4-输出字典-key)
- [题目 5: 输出字符奇数位置的字符串](#题目-5-输出字符奇数位置的字符串)
- [题目 6: 求解100以内的所有素数](#题目-6-求解100以内的所有素数)
- [题目 7: 求矩形面积](#题目-7-求矩形面积)
- [题目 8: 求中位数](#题目-8-求中位数)
- [题目 9: 最大公约数](#题目-9-最大公约数)
- [题目 10: 最小公倍数](#题目-10-最小公倍数)
- [题目 11: 结尾0的个数](#题目-11-结尾0的个数)
- [题目 12: 结尾非零数的奇偶性](#题目-12-结尾非零数的奇偶性)
- [题目 13: 光棍的悲伤 ](#题目-13-光棍的悲伤)

# OJ 网址
[链接](http://www.pythontip.com/coding/code_oj)

看上去好像只支持 Python2.X 的语法, 提交前可到[在线编程](http://www.pythontip.com/coding/run)进行测试

## 题目 1: just print a+b
### 描述
give you two var a and b, print the value of a+b, just do it!!

### 提示
挑战python栏目的所有题目，题目中所给变量使用前不用声明，也不用赋值，系统自动赋值。
如本题，只需一行代码即可： print a + b
系统会自动为a和b赋值，并检查代码执行结果和标准答案是否相同。

### solve
```Python
print(a + b)
```

## 题目 2: list排序
### 描述
给你一个list L, 如 L=[2,8,3,50], 对L进行升序排序并输出,
如样例L的结果为[2,3,8,50]

### solve
```Python
L.sort()
print( L )
```

## 题目 3: 字符串逆序
### 描述
给你一个字符串 a， 如a=‘12345’，对a进行逆序输出a。

### solve
```Python
print(a[::-1])
```

## 题目 4: 输出字典 key
### 描述
给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','链接，如‘1,2,3'。

### solve
```Python
print(",".join([str(i) for i in a]))
```

## 题目 5: 输出字符奇数位置的字符串
### 描述
给你一个字符串 a， 输出字符奇数位置的字符串。如a=‘12345’，则输出135。

### solve
```Python
print(a[::2])
```

## 题目 6: 求解100以内的所有素数
### 描述
输出100以内的所有素数，素数之间以一个空格区分

### solve
```Python
def solve() :
    b = []
    for i in range( 101 ):
        if i == 0 or i == 1 :
            continue
        if is_sushu( i ) :
          b.append( str( i ) )#注意如果用print i,#会导致末尾多了一个空格
    print ' '.join( b )

def is_sushu( num ) :
    for i in range( num ) :
        if i == 0 or i == 1 :
            continue
        if num % i == 0 :
            return False
    return True

solve()
```

## 题目 7: 求矩形面积
### 描述
已知矩形长a,宽b,输出其面积和周长，面积和周长以一个空格隔开

### solve
```Python
print str(a*b),str((a+b)*2)
```

## 题目 8: 求中位数
### 描述
给你一个list L, 如 L=[0,1,2,3,4], 输出L的中位数（若结果为小数，则保留一位小数）。

### solve
```Python
#若有n个数，n为奇数，则选择第（n+1）/2个为中位数，若n为偶数，则中位数是（n/2以及n/2+1）的平均数
#这道题感觉有问题，因为按ac的这种写法，算5.5的话，得到的结果是3位小数，打印出来也是3位小数，不合题意啊
#主要是学一下浮点运算/2.0，其他就算了吧

L.sort()
length = len( L )
if length % 2 != 0 :
    num = L[ length // 2 ]
    if isinstance( num,int ):
        print( num )
    else :
        print( "%.1f" % num )

else :
    num1 = L[ ( length // 2 ) - 1 ]
    num2 = L[ ( length // 2 ) ]
    num = num1 + num2
    print( num / 2.0 )
```

## 题目 9: 最大公约数
### 描述
给你两个正整数a和b， 输出它们的最大公约数。

### solve
```Python
def gcd( x,y ) :
    return x if y == 0 else gcd( y,x % y )
print( gcd( a,b ) ) #a/b不用排序

"""
#同上
while a%b:
    a,b=b,a%b
print b
"""
```

## 题目 10: 最小公倍数
### 描述
给你两个正整数a和b， 输出它们的最小公倍数

### solve
```Python
def gcd( x,y ) :
    return x if y == 0 else gcd( y,x % y )

def lcm( x,y ) :
    return ( x * y ) // gcd( x,y )

print( lcm( a,b ) )
```

## 题目 11: 结尾0的个数 
### 描述
给你一个正整数列表 L, 如 L=[2,8,3,50], 输出L内所有数字的乘积末尾0的个数, 如样例L的结果为2.(提示:不要直接相乘,数字很多,可能溢出)

### solve
```Python
#看了题解：总的来说就是计算除以2和除以5的个数，输出最小的就可以了

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

print( solve( L ) )
```

## 题目 12: 结尾非零数的奇偶性
### 描述
给你一个正整数列表 L, 如 L=[2,8,3,50], 判断列表内所有数字乘积的最后一个非零数字的奇偶性,
奇数输出1,偶数输出0. 如样例输出应为0

### solve
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

print( solve( L ) )
```

## 题目 13: 光棍的悲伤 
### 描述
光棍们对1总是那么敏感，因此每年的11.11被戏称为光棍节。
鄙人光棍几十载，光棍自有光棍的快乐。让我们勇敢面对光棍的身份吧，
现在就证明自己：给你一个整数a，数出a在二进制表示下1的个数，并输出。

### solve
```Python
def solve( num ) :
    return bin( num ).count( "1" )

"""
bin为内置函数，将num转换成二进制数（要求num整数或者包含__index__()方法切返回值为integer的类型）
"""

print( solve( a ) )
```

## 题目 14: Python之美 
### 描述:
输出Python之禅

注意：输出python之禅的源码即可，不用转换为英文。（小小的提示：print this.s)

### solve
```Python
#其实我完全不知道这道题在干啥的
import this
print( this.s )
```

## 题目 15: 大小写转换 
### 描述
给定一个字符串a, 将a中的大写字母 转换成小写，其它字符不变，并输出。

### solve
```Python
print( a.lower() )
```

## 题目 16: 人民币金额打印 
### 描述
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。

在中文大写方式中，0到10以及100、1000、10000被依次表示为：

    零壹贰叁肆伍陆柒捌玖拾佰仟万
    
以下的例子示范了阿拉伯数字到人民币大写的转换规则：

    1	壹圆
    11	壹拾壹圆
    111	壹佰壹拾壹圆
    101	壹佰零壹圆
    -1000	负壹仟圆
    1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 打印出人民币大写表示.

注意：由于中文乱码问题，输出时请先decode("utf8")，例如你要输出ans = "零圆", print ans.decode("utf8").

Note：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。

### solve
```Python
num2chinese = {
    0: "零",
    1: "壹",
    2: "贰",
    3: "叁",
    4: "肆",
    5: "伍",
    6: "陆",
    7: "柒",
    8: "捌",
    9: "玖",
    10: "拾",
    100: "佰",
    1000: "仟",
    10000: "万",
}

def solve(num):
    """
    将数字形式的金额打印成人民币金额
    :param num: 555
    :return: 伍佰伍拾伍圆
    """
    result = str()
    str_num = str(num)

    # 零以及负数处理
    if num == 0:
        result += "零"
    if num < 0:
        result += "负"
        str_num = str_num[1:]

    length = len(str_num)
    # 万圆以上
    if length > 4:
        str_num1 = str_num[: (length - 4)]
        str_num = str_num[(length - 4):]
        result += fun1(str_num1)  # 万左边的数值
        result += "万"
        result += fun1(str_num, True)  # 万右边的数值
    else:
        result += fun1(str_num)
    result += "圆"
    return result


def fun1(num, need_to_print_zero=False):
    num = num.zfill(4)
    result = str()

    # 从千位循环至个位
    for i in range(4, 0, -1):
        temp = int(num) // (10 ** (i - 1))
        if temp != 0:
            result += num2chinese[temp]
            result += num2chinese[10 ** (i - 1)] if i != 1 else str()
            need_to_print_zero = True
        elif need_to_print_zero:
            if int(num) != 0:  # 不是最后一个 0
                result += num2chinese[0]
                need_to_print_zero = False
        num = num[1:]

    return result

print(solve(a))
```

## 题目 17: 公约数的个数
### 描述
给你两个正整数a,b,  输出它们公约数的个数。

## solve
```Python
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

def countGCD(x, y, max_gcd):
    counts = 1
    for i in range(2, max_gcd + 1):
        if x % i == 0 and y % i == 0:
            counts += 1

    return counts

if __name__ == '__main__':
    x, y = 11, 55
    max_gcd = gcd(x, y)
    counts = countGCD(x, y, max_gcd)
    print(counts)
```
