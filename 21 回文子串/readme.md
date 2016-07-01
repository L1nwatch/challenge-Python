## 描述

给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".

## solve
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
    string = "tes112211t112211"
    n = 5
    if huiWenStringExist(string, n):
        print("YES")
    else:
        print("NO")
```