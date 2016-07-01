## 描述

给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。
如：st="00:00:00", et="00:00:10", 则输出10.

## solve
```Python
#一看这题目就知道可以用时间模块
#PS：有模块的坚决不自己写代码
#主要参考题解的两段代码，一段是如何用datatime，另一段是利用map和zip的

"""
import datetime
st=datetime.datetime.strptime(st,"%H:%M:%S")
et=datetime.datetime.strptime(et,"%H:%M:%S")
print (et-st).seconds
"""

#这一段代码略精湛啊，暂时不学了
"""
et = map(int, et.split(":"))
st = map(int, st.split(":"))
dif = 0
for e, s in zip(et, st):
    dif = dif * 60 + (e - s)
print dif
"""
import datetime

et = '23:59:59'
st = '00:00:00'

st = datetime.datetime.strptime(st, "%H:%M:%S")
et = datetime.datetime.strptime(et, "%H:%M:%S")

print((et - st).seconds)
```

## 参考资料
[datetime模块](http://blog.csdn.net/jgood/article/details/5457284)