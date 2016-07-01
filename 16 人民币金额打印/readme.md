## 描述

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

## solve
```Python
cn_num = {
    0:"零",
    1:"壹",
    2:"贰",
    3:"叁",
    4:"肆",
    5:"伍",
    6:"陆",
    7:"柒",
    8:"捌",
    9:"玖",
    10:"拾",
    100:"佰",
    1000:"仟",
    10000:"万",
    }

def solve( num ) :
    result = ""
    str_num = str( num )
    if num == 0 :
        result += "零"
    if num < 0 :
        result += "负"
        str_num = str_num[ 1: ]

    length = len( str_num )
    if length > 4 :
        str_num1 = str_num[ : ( length - 4 ) ]
        str_num = str_num[ ( length - 4 ) : ]
        result += fun1( str_num1 )
        result += "万"
        result += fun1( str_num,True )
    else :
        result += fun1( str_num )
    result += "圆"
    return result


def fun1( num,flag = False ) :
    num_temp = "0000"
    num_temp = num_temp[ :4 - len( num ) ] + num
    num = num_temp
    result = ""
    temp = int( num ) // 1000
    if temp != 0 :
        result += cn_num[temp]
        result += cn_num[1000]
        flag = True
    elif flag == True :
        if int( num ) != 0 :
            result += cn_num[0]
            flag = False

    num = num[ 1: ]
    temp = int( num ) // 100
    if temp != 0 :
        result += cn_num[temp]
        result += cn_num[100]
        flag = True
    elif flag == True :
        if int( num ) != 0 :
            result += cn_num[0]
            flag = False

    num = num[ 1: ]
    temp = int( num ) // 10
    if temp != 0 :
        result += cn_num[temp]
        result += cn_num[10]
        flag = True
    elif flag == True :
        if int( num ) != 0 :
            result += cn_num[0]
            flag = False

    num = num[ 1: ]
    temp = int( num )
    if temp != 0 :
        result += cn_num[temp]
    return result

print( solve( a ).decode( "utf-8") )
```