## OJ 网址
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
