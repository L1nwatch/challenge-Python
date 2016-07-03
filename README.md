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

## solve
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
