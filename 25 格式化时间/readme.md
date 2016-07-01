## 描述

给你一个时间t（t是一个字典，共有六个字符串key(year,month,day,hour,minute,second),值为每个值为数字组成的字符串，
如t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
请将其按照以下格式输出， 格式:XXXX-XX-XX XX:XX:XX。如上例应该输出： 2013-09-30 16:45:02。

## solve
```Python
#虽然可以直接看题解的，不过我还是自己学一下datetime模块后再去看题解吧。
#自己学了一下，有date来表示年月日的，以及time来表示时分秒的

import datetime

#自己实验打印出来明明长得一样，提交上去就是不对我也无语了
#好像自己是因为空格问题，自己手打了个空格后就对了。
if __name__ == '__main__':
    t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
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