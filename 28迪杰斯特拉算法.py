import numpy as np


def dijiesitela(G, start):
    """传入要处理的图和起始节点"""
    dis = list(G[start - 1])
    # 由图初始化起始节点到其余节点的距离
    parents = [-1] * len(dis)
    # 定义列表表示每个节点达到最短距离的父节点,索引表示节点,值表示父节点
    parents[start - 1] = start - 1
    visit = list(dis)
    # 定义还未访问访问确定最短距离的节点
    visit[start - 1] = inf
    # 将起始节点初始化为无穷，visit中的无穷表示访问过确定最短距离的节点
    node = start - 1
    # 初始化处访问节点为初始节点
    for _ in range(len(dis) - 1):
        last_node = node
        # 保存父节点
        shortest_road = min(visit)
        if shortest_road == inf:
            return dis, parents
        # 若最短距离为无穷表明已访问完成,返回dis,后发现不需要了
        node = dis.index(shortest_road)
        # 找出距离起始点最短的为访问过的节点,访问过的已置为inf,所有不会再被访问
        parents[node] = last_node
        # 写入父节点
        visit[node] = inf
        # 将访问过的节点置为inf

        # 处理dis数组,将写入新的最短距离,进行松弛操作
        for i in range(len(dis)):
            if dis[node] + G[node][i] < dis[i]:
                dis[i] = G[node][i] + dis[node]
                visit[i] = G[node][i] + dis[node]

    return dis, parents



def parent_visit(i,parents):
   '''递归输出最短路径'''
   if i==parents[i]:
       print(i+1)
       return 0
   print(i+1,"->",end="")
   parent_visit(parents[i],parents)


if __name__ == "__main__":
    inf = float("inf")
    # 测试用例
    G = [
        [0, 10, inf, 4, inf, inf],
        [10, 0, 8, 2, 6, inf],
        [inf, 8, 0, 15, 1, 5],
        [4, 2, 15, 0, 6, inf],
        [inf, 6, 1, 6, 0, 12],
        [inf, inf, 5, inf, 12, 0],
    ]
    start = 1
    dis, parents = dijiesitela(G, start)

    print("最短路径长度为:")
    for i in dis:
        print(dis.index(i) + 1, "->", start, ":", i)
        # 输出每个节点到起始点的最短距离


    print("所有节点到起始点最短路径为:")
    for i in range(len(G[0])):
        parent_visit(i, parents)