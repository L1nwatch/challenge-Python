## 描述

一个环形的公路上有n个加油站，编号为0,1,2,...n-1,
每个加油站加油都有一个上限，保存在列表limit中，即limit[i]为第i个加油站加油的上限，
而从第i个加油站开车开到第(i+1)%n个加油站需要cost[i]升油,cost为一个列表。
现在有一辆开始时没有油的车，要从一个加油站出发绕这个公路跑一圈回到起点。
给你整数n，列表limit和列表cost,你来判断能否完成任务。
如果能够完成任务，输出起始的加油站编号，如果有多个,输出编号最小的。
如果不能完成任务，输出-1。

## solve
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
    n = 5
    limit = [1, 2, 3, 4, 5]
    cost = [1, 2, 3, 4, 5]
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