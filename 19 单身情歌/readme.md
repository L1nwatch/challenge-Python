## 描述

抓不住爱情的我
总是眼睁睁看它溜走
...

现在来练习一下发现爱的能力，给你一个字符串a,如果其中包含"LOVE"（love不区分大小写)则输出LOVE，否则输出SINGLE。

## solve
```Python
"""
网上好多方法，其中的一些：
正则re.findall
str.index
'LOVE' in string
"""


def isLove(string):
    string = string.upper()
    if string.find("LOVE") != -1:
        return True
    else:
        return False

if __name__ == '__main__':
    a = "LOOLOVVlovE"
    if isLove(a):
        print("LOVE")
    else:
        print("SINGLE")
```