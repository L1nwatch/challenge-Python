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
- [题目 13: 光棍的悲伤](#题目-13-光棍的悲伤)
- [题目 14: Python之美](#题目-14-python之美)
- [题目 15: 大小写转换](#题目-15-大小写转换)
- [题目 16: 人民币金额打印](#题目-16-人民币金额打印)
- [题目 17: 公约数的个数](#题目-17-公约数的个数)
- [题目 18: 逆解最大公约数与最小公倍数](#题目-18-逆解最大公约数与最小公倍数)
- [题目 19: 单身情歌](#题目-19-单身情歌)
- [题目 20: 信息加密](#题目-20-信息加密)
- [题目 21: 回文子串](#题目-21-回文子串)
- [题目 22: 时间就是金钱](#题目-22-时间就是金钱)
- [题目 23: 365 Or 366？](#题目-23-365-or-366)
- [题目 25: 格式化时间](#题目-25-格式化时间)
- [题目 26: 序列判断](#题目-26-序列判断)
- [题目 27: 加油站](#题目-27-加油站)
- [题目 28: 相同数字](#题目-28-相同数字)
- [题目 29: 判断三角形](#题目-29-判断三角形)
- [题目 30: National Day](#题目-30-national-day)
- [题目 31: 山峰的个数](#题目-31-山峰的个数)
- [题目 32: 三角形形状](#题目-32-三角形形状)
- [题目 33: 大幂次运算](#题目-33-大幂次运算)
- [题目 35: 最大连续子序列](#题目-35-最大连续子序列)
- [题目 36: 最大非连续子序列](#题目-36-最大非连续子序列)
- [题目 37: 简单题之勾股定理](#题目-37-简单题之勾股定理)
- [题目 38: 简单题之列表转换](#题目-38-简单题之列表转换)
- [题目 39: 简单题之输出格式练习](#题目-39-简单题之输出格式练习)
- [题目 40: 整数解](#题目-40-整数解)
- [题目 41: Py数](#题目-41-py数)
- [题目 42: 分拆素数和](#题目-42-分拆素数和)
- [题目 43: 斐波那契数列](#题目-43-斐波那契数列)
- [题目 44: 超级楼梯](#题目-44-超级楼梯)
- [题目 45: 砝码问题](#题目-45-砝码问题)
- [题目 46: 取石子游戏](#题目-46-取石子游戏)
- [题目 47: 杨辉三角](#题目-47-杨辉三角)
- [题目 48: 砝码问题II](#题目-48-砝码问题ii)
- [题目 49: 进制转换](#题目-49-进制转换)
- [题目 50: Py扔铅球](#题目-50-py扔铅球)
- [题目 51: 降序排序](#题目-51-降序排序)
- [题目 52: 因子平方和](#题目-52-因子平方和)
- [题目 56: 切西瓜](#题目-56-切西瓜)
- [题目 67: 回文数 I](#题目-67-回文数-i)

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

现在给你一个整数a(``|a| < 100000000``), 打印出人民币大写表示.

注意：由于中文乱码问题，输出时请先``decode("utf8")``，例如你要输出``ans = "零圆"``, ``print ans.decode("utf8")``.

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

### solve
```Python
# 思路很简单, 就是计算出最大公约数之后把每个小于公约数的数都遍历一遍
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

def countGCD(x, y, max_gcd):
    counts = 1
    for i in range(2, max_gcd + 1):
        if x % i == 0 and y % i == 0:
            counts += 1
            
    return counts

max_gcd = gcd(a, b)
counts = countGCD(a, b, max_gcd)
print(counts)
```

## 题目 18: 逆解最大公约数与最小公倍数 
### 描述
我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。
今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。
注：所给数据都有解，不用考虑无解的情况。

### solve
```Python
import math

__author__ = '__L1n__w@tch'


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


def lcm(x, y):
    return x * y / gcd(x, y)


def get_the_two_num(number_gcd, number_lcm):
    a_list = []
    tmp = number_lcm / number_gcd
    for a in range(int(math.sqrt(tmp)), 0, -1):
        if tmp % a == 0:
            b = tmp / a
            if gcd(a, b) == 1:
                a_list.append(a * number_gcd)
                a_list.append(b * number_gcd)
                break

    return a_list


if __name__ == '__main__':
    List = get_the_two_num(a, b)
    List.sort()
    print("%d %d" % (List[0], List[1]))
```

## 题目 19: 单身情歌
### 描述
抓不住爱情的我

总是眼睁睁看它溜走

...

现在来练习一下发现爱的能力，给你一个字符串a,如果其中包含"LOVE"（love不区分大小写)则输出LOVE，否则输出SINGLE。

### solve
```Python
if a.lower().count("love") > 0:
    print("LOVE")
else:
    print("SINGLE")
```

## 题目 20: 信息加密 
### 描述
给你个小写英文字符串a和一个非负数b(``0<=b<26``), 将a中的每个小写字符替换成字母表中比它大b的字母。

这里将字母表的z和a相连，如果超过了z就回到了a。例如``a="cagy",b=3``, 则输出 fdjb

### solve
```Python
def transposition(string, num):
    answer = ""
    for each in string:
        answer += chr((ord(each) - ord('a') + num) % 26 + ord('a'))

    return answer

if __name__ == '__main__':
    string = transposition(a, b)
    print(string)
```

## 题目 21: 回文子串 
### 描述
给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。

回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".

### solve
```Python
def isHuiWen(string):
    return string[::-1] == string

def huiWenStringExist(string, n):
    while len(string) >= n:
        test_string = string[:n]
        if isHuiWen(test_string):
            return True
        else:
            string = string[1:]
    return False

if __name__ == '__main__':
    if huiWenStringExist(a, n):
        print("YES")
    else:
        print("NO")
```

## 题目 22: 时间就是金钱 
### 描述
给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。

如：st="00:00:00", et="00:00:10", 则输出10.

### solve
```Python
#一看这题目就知道可以用时间模块
#PS：有模块的坚决不自己写代码
#主要参考题解的两段代码，一段是如何用datatime，另一段是利用map和zip的

#这一段代码略精湛啊，暂时不学了
"""
et = map(int, et.split(":"))
st = map(int, st.split(":"))
dif = 0
for e, s in zip(et, st):
    dif = dif * 60 + (e - s)
print dif
"""

# 最终提交
import datetime

st = datetime.datetime.strptime(st, "%H:%M:%S")
et = datetime.datetime.strptime(et, "%H:%M:%S")

print((et - st).seconds)
```

### 参考资料
[datetime模块](http://blog.csdn.net/jgood/article/details/5457284)

## 题目 23: 365 Or 366？
### 描述

一年有多少天，这是个大问题，很值得思考。

现在给你一个年份year(year为四位数字的字符串，如"2008","0012"), 你输出这一年的天数。如year="2013", 则输出365。

### solve
```Python
#自己一看的思路就是判断年份是不是闰年，闰年是366剩下的都是365
#先按自己的写一遍再看下题解吧

def is_leap_year(year):
    year = int(year)
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0 ):
        return True
    else:
        return False

if __name__ == '__main__':
    if is_leap_year(year):
        print("366")
    else:
        print("365")

"""
题解的datetime库解决法：
def year(years):
 import datetime,time
 y1 = datetime.datetime(years,1,1)
 y2 = datetime.datetime(years+1,1,1)

 print str(y2 - y1).split(' ')[0]

学习了，实际上,y2 - y1 返回的是datetime 的类型 timedelta 时间差
直接改成 （y2 - y1）. days 就好了
"""
```

## 题目 25: 格式化时间
### 描述
给你一个时间t（t是一个字典，共有六个字符串key(year,month,day,hour,minute,second),值为每个值为数字组成的字符串，如 t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}

请将其按照以下格式输出， 格式:XXXX-XX-XX XX:XX:XX。如上例应该输出： 2013-09-30 16:45:02。

### solve
```Python
#虽然可以直接看题解的，不过我还是自己学一下datetime模块后再去看题解吧。
#自己学了一下，有date来表示年月日的，以及time来表示时分秒的

import datetime

#自己实验打印出来明明长得一样，提交上去就是不对我也无语了
#好像自己是因为空格问题，自己手打了个空格后就对了。
if __name__ == '__main__':
    # t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
    test = datetime.date(int(t['year']), int(t['month']), int(t['day']))
    test_2 = datetime.time(int(t['hour']), int(t['minute']), int(t['second']))
    print(str(test) + " " + str(test_2))


"""
看下题解的写法：
from datetime import datetime
for k, v in t.items():
    t[k] = int(v) #这个转换的方法得学下，要不然每个都得加个int累死了
    #下面的datetime居然能有这么多，学习了
dt = datetime(t['year'], t['month'], t['day'], t['hour'], t['minute'], t['second'])
print dt.strftime("%Y-%m-%d %X")

datetime.strptime(date_string, format)：将格式字符串转换为datetime对象；
"""
```

## 题目 26: 序列判断
### 描述
给你一个整数组成的列表L，按照下列条件输出：
若L是升序排列的,则输出"UP";

若L是降序排列的,则输出"DOWN";

若L无序，则输出"WRONG"。

### solve
```Python
# 最终提交
if sorted(L)==L:
    print "UP"
elif sorted(L)[::-1]==L:
    print "DOWN"
else:
    print "WRONG"

# -----上面的答案比我的简洁好多------

#没想到好办法，自己遍历着来判断一下吧
#如果题解有更好的方法自己再学习吧

def isUpList(List):
    new_List = List.copy()  #2.X版本提示说没有copy这个方法，所以得用List[:]来复制
    new_List.sort()
    if new_List == List:
        return True
    else:
        return False

def isDownList(List):
    new_List = List.copy() #copy.deepcopy(L)，这个方法也是可以的
    new_List.sort(reverse = True)
    if new_List == List:
        return True
    else:
        return False

if __name__ == '__main__':
    L = [3, 2]
    if isUpList(L):
        print("UP")
    elif isDownList(L):
        print("DOWN")
    else:
        print("WRONG")
```

## 题目 27: 加油站 
### 描述
一个环形的公路上有n个加油站，编号为0,1,2,...n-1,每个加油站加油都有一个上限，保存在列表limit中，即limit[i]为第i个加油站加油的上限，而从第i个加油站开车开到第(i+1)%n个加油站需要cost[i]升油,cost为一个列表。

现在有一辆开始时没有油的车，要从一个加油站出发绕这个公路跑一圈回到起点。

给你整数n，列表limit和列表cost,你来判断能否完成任务。

如果能够完成任务，输出起始的加油站编号，如果有多个,输出编号最小的。

如果不能完成任务，输出-1。

### solve
```Python
#遍历一下就出来答案了吧这题看着。。。
#交上去一次性成功了。。。没测试答案心里虚虚的。。

def canFinishTheWork(n, limit, cost, i):
    bus_gas = 0
    order = i
    while True:
        bus_gas += limit[i]
        if bus_gas < cost[i]:
            return False
        else:
            bus_gas -= cost[i]
        i = (i + 1) % n
        if i == order:
            break
    return True

if __name__ == '__main__':
    # n = 5
    # limit = [1, 2, 3, 4, 5]
    # cost = [1, 2, 3, 4, 5]
    List = []
    for i in range(n):
        if canFinishTheWork(n, limit, cost, i):
            List.append(i)

    List.sort()
    if len(List) <= 0:
        print("-1")
    else:
        print(List[0])
```

## 题目 28: 相同数字 
### 描述
给你一个整数列表L,判断L中是否存在相同的数字，若存在，输出YES，否则输出NO。

### solve
```Python
#一上来两个思路，一个是转换成set集合再比较长度，另一个是遍历一遍

def hasSameNum(List):
    return len(set(List)) != len(List)

if __name__ == '__main__':
    # L = [1, 2, 3]
    if hasSameNum(L):
        print("YES")
    else:
        print("NO")
```

## 题目 29: 判断三角形
### 描述
给你三个整数a,b,c,  判断能否以它们为三个边长构成三角形。

若能，输出YES，否则输出NO。

### solve
```Python
#三角形两边之和大于第三边，两边之差小于第三边
#一次性AC

"""
关于判定定理的问题，这里有两种说法：
legend_001 评论于 2014-07-12 11:33:30
先sort，然后保证前两个的和大于第三个就好，因为sort之后就保证了前两个的差小于第三个
ylgkger 评论于 2014-12-19 19:10:27
简化 a+b+c-max(a,b,c)*2>0即可
"""

def canBeTriangle(a, b, c):
    List = [a, b, c]
    List.sort()
    return (List[0] + List[1] > List[2]) and (List[2] - List[0] < List[1])

if __name__ == '__main__':
    # a, b, c = 3, 4, 5
    if canBeTriangle(a, b, c):
        print("YES")
    else:
        print("NO")
```

## 题目 30: National Day
### 描述:
马上国庆节了，用一个英文单词描述你此时此刻的心情。

### solve
```Python
print("Happy")
```

## 题目 31: 山峰的个数
### 描述
十一假期,小P出去爬山,爬山的过程中每隔10米他都会记录当前点的海拔高度(以一个浮点数表示),这些值序列保存在一个由浮点数组成的列表h中。回到家中，小P想研究一下自己经过了几个山峰，请你帮他计算一下，输出结果。

例如：h=[0.9,1.2,1.22,1.1,1.6,0.99], 将这些高度顺序连线，会发现有两个山峰，故输出一个2(序列两端不算山峰)

### solve
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
    # h = [0.9, 1.2, 1.22, 1.1, 1.6, 0.99]
    print(countNumOfPeaks(h))
```

## 题目 32: 三角形形状
### 描述:
给以一个三角形的三边长a,b和c(边长是浮点数),请你判断三角形的形状。

若是锐角三角形，输出R;

若是直角三角形，输出Z;

若是钝角三角形，输出D;

若三边长不能构成三角形，输出W.

### solve
```Python
#自己想到的思路是用余弦定理
#baidu了一下，发现是用最大边所对应的角来计算
"""
若最大边的平方等于另两边的平方和,则它为直角三角形;
若最大边的平方大于另两边的平方和,则它为钝角三角形;
若最大边的平方小于另两边的平方和,则它为锐角三角形.
"""

def canBeTriangle(a, b, c):
    List = [a, b, c]
    List.sort()
    if (List[0] + List[1] > List[2]) and (List[2] - List[0] < List[1]):
        return True
    else:
        return False

def getTypeOfTriangle(a, b, c):
    List = [i ** 2 for i in [a, b, c]]
    List.sort()
    result = List[2] - List[1] - List[0]
    if result == 0:
        return "Z"
    elif result < 0:
        return "R"
    elif result > 0:
        return "D"

if __name__ == '__main__':
    # a, b, c = 3, 4, 5
    if canBeTriangle(a, b, c) == False:
        print("W")
    else:
        print(getTypeOfTriangle(a, b, c))
```

## 题目 33: 大幂次运算
### 描述:
给你两个正整数a(``0 < a < 100000``)和n(``0 <= n <=100000000000``)，计算``(a^n) % 20132013``并输出结果

### solve
```Python
def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e&1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b*b) % m
    return result

# a, n = 5, 6
print(fastExpMod(a, n, 20132013))
```
======================上面也是快速幂取模，跑起来对的！！！=========================
***

### solve2
```Python
#之前ACM有做过，就是求模公式呗
"""
翻一下acm笔记：
(a * a) % m = ( a % m * a % m ) % m
"""

#看了下题解，说是快速幂（之前ACM刷斐波那契的时候应该遇到过了，就是二分矩阵快速求幂）
#直接看题解报告了，自己写出算法是不太可能的。。。
#题解。。。。牛过头了：print(pow(a, n, 20132013))

"""
以下说是快速幂取模：
a^b mod c = ((a^2)^(b / 2)) mod c, b是偶数
a^b mod c = ((a^2)^(b / 2) * a) mod c, b是奇数

#下面的代码，在自己的机子上跑着是错的，但是在网上跑的确是对的？python版本的问题我估计！
def PowerMod(a, n, ret):
    if n == 0:
        return ret
    if n % 2:
        ret = ret * a % 20132013

    return PowerMod( a * a % 20132013, n / 2, ret)

if __name__ == '__main__':
    a, n = 5, 6
    ret = 1
    print(PowerMod(a, n, ret))
"""
```

### run time error
```Python
"""
version 1
说是算法超时了...
O(n)算法说我超时了，好吧，看来只能看题解了
def solve(a, n):
    result = 0
    if n == 0:
        result = 1
    else:
        result = a % 20132013
        n -= 1

    while n > 0:
        n -= 1
        result = (result * (a % 20132013)) % 20132013

    return result

if __name__ == '__main__':
    a, n = 5, 5
    print(solve(a, n))
"""
```

## 题目 35: 最大连续子序列 
### 描述:
给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个连续子序列，使其和最大，输出最大子序列的和。

例如，对于L=[2,-3,3,50]， 输出53（分析：很明显，该列表最大连续子序列为[3,50]).

### solve
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
    # L = [2, -3, 3, 50]
    print(getLargestSum(L))
```

## 题目 36: 最大非连续子序列 
### 描述:
给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个非连续子序列，使其和最大，输出最大子序列的和。

这里非连续子序列的定义是，子序列中任意相邻的两个数在原序列里都不相邻。

例如，对于L=[2,-3,3,50]， 输出52（分析：很明显，该列表最大非连续子序列为[2,50]).

### solve
```Python
#个人的思路是依旧利用动态规划，状态方程为：
#b[j] = max(b[j - 2] + List[j], b[j - 1], List[j])

def solve(List):
    L = List[:] # 没有 List.copy(), 用 List[:] 替代了
    if len(List) > 1:
        L[1] = max(List[0], List[1])
    for i in range(2, len(List)):
        L[i] = max(L[i - 2] + List[i], L[i - 1], List[i])

    return L[-1]

if __name__ == '__main__':
    # L = [8, -3, 2, -3, 3, 60, -100, 50]
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

## 题目 37: 简单题之勾股定理
### 描述
给你直角三角形的两个直角边的边长a,b,请你求出其斜边边长，结果保留小数点后三位小数。

如a=3, b =4, 则输出5.000。

### solve
```Python
#勾股定理的公式不就是c^2 = a^2 + b^2么
#print '%.3f' %(a**2+b**2)**0.5

def getC(a, b):
    c = a ** 2 + b ** 2
    return c ** 0.5

if __name__ == '__main__':
    # a, b = 3, 4
    answer = getC(a, b)
    print(format(answer, '.3f'))
```

## 题目 38: 简单题之列表转换
### 描述
给你一个字符串列表L，请用一行代码将列表所有元素拼接成一个字符串并输出。

如L=['abc','d','efg'], 则输出abcdefg。

### solve
```Python
#题目要求一行代码，吓~~~

# L=['abc','d','efg']
print(''.join([str(i) for i in L])) #这句好了，在2.X版本下
#题解更简单：
print(''.join(L))

#下面这句在python3.X版本倒是对了，2.X自己报语法错误了
[print(i, end = "") for i in L]
```

## 题目 39: 简单题之输出格式练习 
### 描述

给你一个字符串列表L，用一行代码顺序输出L中的元素，元素之间以一个空格隔开，注意行尾不要有空格，输出单独占一行。
如L=['abc','d','efg'], 则输出abc d efg。

### solve
```Python
#又是一行代码，吓~~
#思路跟上一题一样呗，2.X版本下用join函数, 3.X版本下print(i, end=' ')

# L = ['abc', 'd', 'efg']
print(' '.join(L))
```

## 题目 40: 整数解 
### 描述
给你两个整数a和b（``-10000<a,b<10000``），请你判断是否存在两个整数，他们的和为a，乘积为b。

若存在，输出Yes,否则输出No

例如：``a=9,b=15``, 此时不存在两个整数满足上述条件，所以应该输出No。

### solve
```Python
#看到a和b那么小，一下子就想遍历了。。。
#看version 1的遍历，一下子就超时了，说明不行
#x + y = a, x * y = b ==> x * ( a - x ) = b，这样就只有一层遍历了

#看题解居然使用解方程的方法
#题解的时间复杂度为O(1)啊，醉了：
#两个数应该为方程x^2 - a*x + b = 0 的解，判断delta即可

def isExist(a, b):
    for i in range(-9999, 10000):
        if i * ( a - i ) == b:
            return True

    return False

if __name__ == '__main__':
    # a, b = 9, 15
    if isExist(a, b):
        print("Yes")
    else:
        print("No")

"""
---version 2---
题解：
from math import sqrt
delta = a*a - 4*b
if delta > 0 and int(sqrt(delta)) == sqrt(delta):
    print "Yes"
else:
    print "No"
"""

"""
---version 1---
def isExist(a, b):
    for i in range(-9999, 10000):
        for j in range(-9999, 10000):
            if i + j == a and i * j == b:
                return True

    return False
"""
```

## 题目 41: Py数
### 描述
Py从小喜欢奇特的东西，而且天生对数字特别敏感，一次偶然的机会，他发现了一个有趣的四位数2992，这个数，它的十进制数表示，其四位数字之和为2+9+9+2=22，它的十六进制数BB0，其四位数字之和也为22，同时它的十二进制数表示1894，其四位数字之和也为22，啊哈，真是巧啊。

Py非常喜欢这种四位数，由于他的发现，所以这里我们命名其为Py数。

现在给你一个十进制4位数n，你来判断n是不是Py数，若是，则输出Yes，否则输出No。

如n=2992，则输出Yes； n = 9999，则输出No。

### solve
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

print conv(n,16) == conv(n,12) == conv(n,10) and 'Yes' or 'No' # 居然利用短路逻辑了
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
    # num = 2992
    if isPyNum(n):
        print("Yes")
    else:
        print("No")
```

## 题目 42: 分拆素数和
### 描述
把一个偶数拆成两个不同素数的和，有几种拆法呢？

现在来考虑考虑这个问题，给你一个不超过10000的正的偶数n，计算将该数拆成两个不同的素数之和的方法数，并输出。

如n=10，可以拆成3+7，只有这一种方法，因此输出1.

### solve
```Python
#个人思路，遍历一遍10000以内的素数。
#然后我就得先有个10000以内的素数表

#自己的方法虽然过了，但是个人觉得时间复杂度应该会高些，毕竟是O(n)算法
"""
以下看下题解吧：
看了题解，比较喜欢的是这个(利用哈希表而不是列表这样时间复杂度快了N多)：
def sushuDic(n):
    dic = {x: True for x in range(2, n)}
    for x in dic.keys():
        if dic[x]:
            i = x * 2
            while i < n:
                dic[i] = False
                i = i + x
    return dic


def divideCnt(n):
    dic = sushuDic(n)
    cnt = 0
    for i in range(2, n // 2):
        if dic[i] and dic[n-i]:
            cnt = cnt + 1
    return cnt

print divideCnt(n)

用哈希表快速求素数。
"""
import  math

def createPrimeList(num):
    List = []

    for i in range(2, num):
        prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            List.append(i)

    return List

def countWays(num, prime_list):
    counts = 0
    for each in prime_list:
        if each >= num:
            break
        elif each != (num - each) and (num - each) in prime_list:
            counts += 1

    return counts // 2

if __name__ == '__main__':
    prime_list = createPrimeList(10000)
    # n = 10
    ways = countWays(n, prime_list)
    print(ways)
```

## 题目 43: 斐波那契数列
### 描述
斐波那契数列为1,1,2,3,5,8...。数列从第三项起满足，该项的数是其前面两个数之和。

现在给你一个正整数n（n < 10000), 请你求出第n个斐波那契数取模20132013的值（斐波那契数列的编号从1开始）。
### solve
```Python
#这道题我还是搬ACM的题解吧，毕竟之前用那个方法（C++下的）过了2ms的题
#所以算法时间复杂度绝对是可以的

#以下：f[n] = f[n - 1] + f[n - 2]
#附算法网址：http://www.acmerblog.com/fibonacci-3395.html

"""
题解用的迭代：
def count(n):
    x = [0,1]
    for i in range(2,n+1):
        x.append(x[i-1] + x[i-2])
    return x[n]

print count(n)%20132013
"""

def multiply(c, a, b, mod):
    tmp = [ a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1] ]
    c[0][0] = tmp[0] % mod
    c[0][1] = tmp[1] % mod
    c[1][0] = tmp[2] % mod
    c[1][1] = tmp[3] % mod

def fibonacci(n, mod):
    if n == 0:
        return 0
    elif n <= 2:#这里表示第0项为0，第1，2项为1
        return 1

    a = [[1, 1], [1, 0]]
    result = [[1, 0], [0, 1]]
    n -= 2
    while n > 0:
        if n % 2 == 1:
            multiply(result, result, a, mod)
        multiply(a, a, a, mod)
        n //= 2 #注意这里不能写n /= 2,得用地板除法

    s = (result[0][0] + result[0][1]) % mod
    return s

if __name__ == '__main__':
    mod = 20132013
    answer = fibonacci(n, mod)
    print(answer)
```

## 题目 44: 超级楼梯
### 描述
有一楼梯共n级，刚开始时你在第一级，若每次只能跨上一级或二级，要走上第n级，共有多少种走法？

现在给你一个正整数n（``0<n<40``),请你输出不同的走法数。

如``n=2``,则输出1（你只有一种走法，走一步，从第一级到第二级）

### solve
```Python
#这道题不就是斐波那契么，= =我觉得是
#f[n] = f[n - 1] + f[n - 2]
#因为n比较少，所以我用迭代吧

"""
另一种迭代的表达形式：
a = 1
b = 2
for i in range(1, n-1):
    c = a + b
    a = b
    b = c
print a
"""

def fibonacci(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])

    return f[-1]

if __name__ == '__main__':
    # n = 4
    print(fibonacci(n))
```

## 题目 45: 砝码问题
### 描述
有一组砝码，重量互不相等，分别为m1、m2、m3……mn；它们可取的最大数量分别为x1、x2、x3……xn。

现要用这些砝码去称物体的重量,问能称出多少种不同的重量。

现在给你两个正整数列表w和n， 列表w中的第i个元素w[i]表示第i个砝码的重量，列表n的第 i 个元素 n[i] 表示砝码i的最大数量。i从0开始，请你输出不同重量的种数。

如：w=[1,2], n=[2,1], 则输出5（分析：共有五种重量：0,1,2,3,4）

### solve
```Python
#为啥我看到这种问题，第一眼想到的是背包问题。
#不浪费时间，果断看题解

#喵了一遍题解，DP+遍历的说？
#自己的思路有三种循环。
#一次性过了，简述一下思路吧，第一个循环表示每一个砝码来一次，第二个循环表示
#该砝码从1个取到n[i]个，第三个循环表示上一个的所有情况每个都取一下然后再来+现在的这个

#感觉自己的代码时间复杂度很大，不是一般的大！

def solve(w, n):
    total = set()
    total.add(0)
    length = len(w)
    for i in range(length):
        tmp_set = set()
        for j in range(1, n[i] + 1):
            for each in total:
                tmp = each + j * w[i]
#                print("i = {0}, j = {1}, each = {2}, tmp = {3}"\
#                      .format(i, j, each, tmp))
                if tmp not in total:
                    tmp_set.add(tmp)
        total.update(tmp_set)

    return total

if __name__ == '__main__':
    # w = [1, 2]
    # n = [2, 1]
    print(len(solve(w, n)))

"""
题解的：
---version 1---
total_w=0
length_n=len(w)
for i in range(length_n):
    total_w+=w[i]*n[i]
S=set([])
S.add(total_w)
for i in range(length_n):
    temp_S=S.copy()
    for s in temp_S:
        j=1
        while j<=n[i]:
            S.add(s-j*w[i])
            j+=1
print len(S)

---version 2---
若m1能被称出，则total_w-m1亦能被称出，如此，可以稍作优化：

total_w=0
length_n=len(w)
for i in range(length_n):
    total_w+=w[i]*n[i]
S=set([])
S.add(total_w)
for i in range(length_n):
    temp_S=S.copy()
    for s in temp_S:
        j=1
        while j<=n[i]:
            if s-j*w[i]>=total_w/2:
                S.add(s-j*w[i])
                S.add(total_w-s+j*w[i])
                j+=1
            else:
                break
print S
print len(S)
"""
```

## 题目 46: 取石子游戏
### 描述
有两堆石子，数量任意，可以不同。游戏开始由两个人轮流取石子。游戏规定，每次有两种不同的取法，一是可以在任意的一堆中取走任意多的石子；二是可以在两堆中同时取走相同数量的石子。最后把石子全部取完者为胜者。

现在给出初始的两堆石子的数目a和b，如果轮到你先取，假设双方都采取最好的策略，问最后你是胜者还是败者。

如果你是胜者，输出Win,否则输出Loose。

例如，a=3,b=1, 则输出Win(你先在a中取一个，此时a=2，b=1,此时无论对方怎么取，你都能将所有石子都拿走).

### solve
```Python
#之前在ACM课上听过，这是博弈论的东西
#查了一下，是威佐夫博奕
#ACM解题报告：http://blog.csdn.net/csust_acm/article/details/7957180

import math

def solve(a, b):
    '面对非奇异局势，先拿者必胜；反之，则后拿者取胜。'
    a, b = min(a, b), max(a, b) #奇异局势下，bk > ak
    k = b - a #奇异局势下，bk = ak + k
    m = int((math.sqrt(5.0) + 1) * k / 2) #奇异局势下，ak = 这个公式
    return m != a #若m == a，则为奇异局势，先拿者必败

if __name__ == '__main__':
    #a, b = 3, 1
    #a, b = 2, 1
    #a, b = 8, 4
    #a, b = 4, 7
    if solve(a, b):
        print("Win")
    else:
        print("Loose")

"""
题解用到了奇异态势，并不好理解。
相关分析参考：http://blog.renren.com/share/251405117/755224137

推出一个概念：奇异态势。有以下特点：

1.无法从一个奇异态势一步走到另一个奇异态势；

2.任何非奇异态势可以一步走到某一个奇异态势。

于是可构建以下奇异态势，前几组分别为(0,0),(1,2),(3,5),(4,7),(6,10),(8,13)....满足：1）各奇异态势间无重复元素；2）步长（|a-b|）递增，保证各不相同

以此可以计算出(a,b)以下的奇异态势，若(a,b)不在其中，则必赢。

题解代码：
m,n=max(a,b),min(a,b)
small_num=0
large_num=0
step=0
S=set([])
S.add(small_num)
S.add(large_num)
Win=True
while small_num<n and large_num<m:
    while small_num in S:
        small_num+=1
    step+=1
    large_num=small_num+step
    S.add(small_num)
    S.add(large_num)
    if small_num==n and large_num==m:
        Win=False
        break
#    print '('+str(small_num)+','+str(large_num)+')'
if Win:
    print 'Win'
else:
    print 'Loose'
"""
```

## 题目 47: 杨辉三角
### 描述:
还记得中学时候学过的杨辉三角吗？具体的定义这里不再描述，你可以参考以下的图形：

    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    1 5 10 10 5 1
    ..............
    
先在给你一个正整数n，请你输出杨辉三角的前n层
注意：层数从1开始计数,每层数字之间用一个空格隔开，行尾不要有空格。
如``n=2``,则输出：

    1
    1 1

### solve
```Python
def getNum(row, col, num):
    if col == 0 or col == row:
        num[row][col] = 1
    if num[row][col] == -1:
        num[row][col] = getNum(row - 1, col - 1, num) + \
                        getNum(row - 1, col, num)

    return num[row][col]

def solve(n, num_array):
    for i in range(n):
        for j in range(i):
            print(getNum(i, j, num_array)),
        print(getNum(i, i, num_array))

def createNumArray(n):
    num = []
    for i in range(n):
        num.append([-1 for i in range(n)])

    return num

if __name__ == "__main__":
    num_array = createNumArray(n)
    solve(n, num_array)
```

## 题目 48: 砝码问题II
### 描述
有一组砝码，重量互不相等，分别为m1、m2、m3……mn；每种砝码的数量有无限个。

现要用这些砝码去称物体的重量,给你一个重量n,请你判断有给定的砝码能否称出重量n。

现在给你一个正整数列表w和一个正整数n，列表w中的第i个元素w[i]表示第i种砝码的重量，n 表示要你判断的重量。如果给定砝码能称出重量n，输出Yes，否则输出No。

例如，w=[2,5,11], n=9,则输出Yes（取两个2，一个5）。

### solve
```Python
#悲催了，用别人的也是超时了，改进一下之前的吧，不求出全部了，一求到那个就返回True
#这下成功了

def getWeightList(w, amount, n):
    total = set()
    total.add(0)
    length = len(w)
    for i in range(length):
        tmp_set = set()
        for j in range(1, amount[i] + 1):
            for each in total:
                tmp = each + j * w[i]
                if tmp == n:
                    return True
#                print("i = {0}, j = {1}, each = {2}, tmp = {3}"\
#                      .format(i, j, each, tmp))
                if tmp not in total:
                    tmp_set.add(tmp)
        total.update(tmp_set)

    return False

def getMaxAmount(w, n):
    amount = []
    for each in w:
        amount.append(n // each)

    return amount

if __name__ == "__main__":
    # w = [2, 5, 11]
    # n = 9
    amount = getMaxAmount(w, n)
    if getWeightList(w, amount, n):
        print("Yes")
    else:
        print("No")

"""
题解：
---version 1---
完全背包:

L=len(w)
s=[-1 for i in range(n+1)]
s[0]=0
for i in range(L):
    for j in range(1,n+1):
        if j-w[i]>=0 and s[j-w[i]]!=-1:
            s[j]=1
if s[n]!=-1:
    print 'yes'
else:
    print "no"

"""
```

## 题目 49: 进制转换
### 描述
给你一个十进制数a，将它转换成b进制数,如果 ``b>10``,用大写字母表示（10用A表示，等等）

a为32位整数，``2 <= b <= 16``

如 a = 3, b = 2, 则输出 11

### solve
```Python
#基本思路是除b取余法
#搞了半天错误的原因是没处理负数情况，醉了。。。

def solve(num, n):
    character = "0123456789ABCDEF"
    answer = ""
    if num < 0:
        symbol = "-"
        num = -num
    else:
        symbol = ""
    while num > 0:
        answer += character[num % n]
        num //= n

    return symbol + answer[::-1]

if __name__ == "__main__":
    # a, b = -100, 16
    print(solve(a, b))

"""
题解：
---version 1---
d = '0123456789ABCEDFGHIJKLMNOPQRSTUVWXYZ'
def f(x,y):
    s = []
    while x>=y:
        s.append(x%y)
        x /=y
    s.append(x)
    return ''.join([d[c] for c in s[::-1]])

print (a<0 and '-' or '')+f(abs(a),b)
"""
```

## 题目 50: Py扔铅球
### 描述
Py不但是编程大牛，而且是运动健将。比如说扔铅球，1000m，现在Py参加校园扔铅球比赛，给你Py的身高a（双精度数），球落地点与Py头部的连线与水平线的夹角 b（弧度），要你编写一个程序计算Py扔铅球的水平距离。

a，b都是浮点数，注意b是弧度，其中， ``140 < a < 200,  0 < b < 1.5``.

输出你求出的水平距离，保留到小数点后三位。

如，a = 165.5, b = 1.1, 则输出 84.234

### solve
```Python
#思路：画一下图，易得a/x = tanb(θ)
#format函数参考：http://pyformat.info/

import math

def solve(a, b):
    answer = a / math.tan(b)    #注意math.tan(b)本来就要求弧度制而不是角度!
    return answer

if __name__ == "__main__":
    a, b = 165.5, 1.1
    print('{:.3f}'.format(solve(a, b)))
```

## 题目 51: 降序排序
### 描述
给你一个list L, 如 L=[2,8,3,50], 对L进行降序排序并输出,如样例L的结果为[50,8,3,2]

### solve
```Python
if __name__ == "__main__":
    # L = [2,8,3,50]
    L.sort(reverse = True)
    print(L)
```

## 题目 52: 因子平方和
### 描述
6 的因子有 1, 2, 3 和 6, 它们的平方和是 ``1 + 4 + 9 + 36 = 50``. 

如果 f(N) 代表正整数 N 所有因子的平方和, 那么 f(6) = 50.

现在令 F 代表 f 的求和函数, 亦即 ``F(N) = f(1) + f(2) + .. + f(N)``, 显然 F 一开始的 6 个值是: 1, 6, 16, 37, 63 和 113.

那么对于任意给定的整数 N (``1 <= N <= 10^8``), 输出 F(N) 的值.

### solve
```Python
#目测自己的算法会超时
#思路：一个函数用于求因子，一个函数用于求因子的和f(N)，一个函数用于求F(N)
#果然超时了。

"""
附题解2个，自己还没解决出来：
---version 1---


这道题直接做回超时。

技巧一：F(N)可以看作N个1*＊2，N/2个2*＊2，N/3个3＊＊2，，，，，以此类推。即便这样，还会超时。

技巧二：对称。N个1*＊2对称1个N**2，N/2个2*＊2对称2个N/2**2,,,,,,. 但是，值得注意的是对称并不是一对一的，而是一对多的。比如N个1*＊2对称的是1个 (N/2**2,,,,,,,(N-1)**2，N**2］。依次类推。

import math
def sumsqr(m, n):
    if m >= n:
        return 0
    return n*(n+1)*(2*n+1)/6-m*(m+1)*(2*m+1)/6
def F(n):
    i=1
    seg=[]
    sum1=0
    high = n;
    while i*i <=n:
        sum1 += (n/i)*i**2
        low = max(n/(i+1), i);
        sum1 += i*sumsqr(low,high)
        i += 1
        high = low
    return sum1

F(N)
计算清楚每个N**2序列的个数即可

def func(N):
    result=0
    n=N+1
    a,b=0,0
    while n>1:
        n=N/(N/n+1)
        a,b=N/n,a
        print n
        result+=(a-b)*n*(n+1)*(2*n+1)/6
print func(N)
sorry，贴错了~更新下：

def func(N):
    result=0
    n=N+1
    a,b=0,0
    while n>1:
        n=N/(N/n+1)
        a,b=N/n,a
        result+=(a-b)*n*(n+1)*(2*n+1)/6
    return result
print func(N)

---version 2---
#N = 2

def cal(x):
    return x * (x + 1) * (2 * x + 1) / 6

ans = 0

for i in range(1, N / 10 + 1):
    ans += (N / i) * i * i
for i in range(9, 0, -1):
    ans += i * (cal(N / i) - cal(N / (i + 1)))
print ans


"""

def getDivisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors

def getDivisorsSum(num):
    divisors = getDivisors(num)
    answer = 0
    for each in divisors:
        answer += each ** 2

    return answer

def getTotalDivisorsSum(num):
    answer = 0
    for i in range(num):
        answer += getDivisorsSum(i + 1)

    return answer

if __name__ == "__main__":
    for N in range(1, 8):
        print(getTotalDivisorsSum(N))
```

## 题目 56: 切西瓜
### 描述
小Py要吃西瓜，想知道切了n刀后，最多能切出多少块？请你们帮助下小Py.

给你一个正整数n（0 < n < 10^3),你输出一个数字，代表最多能切多少块。

如n=1, 输出2。

### solve
```Python
#通过n条直线，最多可将一个平面分割成1+（1+n）n/2
#后面才看到这应该是三维平面里的公式才能：Y = (X ** 3 +5 * X + 6) / 6

"""
题解还有另外一个公式：
C(n,0)+C(n,1)+C(n,2)+C(n,3)
"""

def spaceSubdivide(n):
    return int((n ** 3 + 5 * n + 6) / 6)

if __name__ == "__main__":
    # n = 1
    print(spaceSubdivide(n))
```

## 题目 67: 回文数 I
### 描述
若一个数（首位不为0）从左到右读与从右到左读都是一样，这个数就叫做回文数，例如12521就是一个回文数。

给定一个正整数，把它的每一个位上的数字倒过来排列组成一个新数，然后与原数相加，如果是回文数则停止，如果不是，则重复这个操作，直到和为回文数为止。给定的数本身不为回文数。

例如：87则有：

    STEP1: 87+78=165
    STEP2: 165+561=726
    STEP3: 726+627=1353
    STEP4: 1353+3531=4884

现在给你一个正整数M（``12 <= M <= 100``),输出最少经过几步可以得到回文数。如果在8步以内（含8步）不可能得到回文数，则输出0。

例如：M=87，则输出4.

### solve
```Python
#感觉是遍历一遍就出来了

def countTimes(num):
    counts = 0
    while counts <= 8:
        counts += 1
        num = int(str(num)[::-1]) + num
        if isHuiWen(num):
            return counts
    else:
        return 0

def isHuiWen(num):
    return str(num)[::-1] == str(num)

if __name__ == "__main__":
    # M = 87
    print(countTimes(M))

"""
题解
---version 1---
flag = 0
for i in range(8):
    M = M + int(str(M)[::-1])
    if str(M) == str(M)[::-1]:
        flag = i + 1
        break
print flag
---version 2---
fg=0
while fg<8:
    S=int(str(M)[::-1])
    D=S+M
    fg += 1
    if D==int(str(D)[::-1]):
        print fg
        break
    else:
        M=D
else:
    print 0
"""
```
