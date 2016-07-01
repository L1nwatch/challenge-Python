## 描述

给你一个整数组成的列表L，按照下列条件输出：
若L是升序排列的,则输出"UP";
若L是降序排列的,则输出"DOWN";
若L无序，则输出"WRONG"。

## solve
```Python
if sorted(L)==L:
    print "UP"
elif sorted(L)[::-1]==L:
    print "DOWN"
else:
    print "WRONG"

-----上面的答案比我的简洁好多------

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