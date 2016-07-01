## 描述

一年有多少天，这是个大问题，很值得思考。现在给你一个年份year(year为四位数字的字符串，如"2008","0012"),
你输出这一年的天数。如year="2013", 则输出365。

## solve
```Python
#自己一看的思路就是判断年份是不是闰年，闰年是366剩下的都是365
#先按自己的写一遍再看下题解吧

def isBissextile(year):
    year = int(year)
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0 ):
        return True
    else:
        return False

if __name__ == '__main__':
    year = "2008"
    if isBissextile(year):
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