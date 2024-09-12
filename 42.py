class MGraphNode:
    def __init__(self, kMaxVertex, no_edge_value, directed) -> None:
        self.n_verts = 0  # 顶点数
        self.m_edges = 0  # 边数
        self.edge_matrix = [[no_edge_value] * kMaxVertex for _ in range(kMaxVertex)]  # 邻接矩阵
        self.ver_list = [None] * kMaxVertex  # 存储顶点信息
        self.no_edge_value = no_edge_value  # 表示没有边时的权重值
        self.directed = directed  # true为有向图，false为无向图

    # 算法7-1: 获取图的顶点个数 NumberOfVerts(graph)
    def NumberOfVerts(self):
        return self.n_verts

    # 算法7-2: 判断边是否存在 ExistEdge(graph, u, v)
    def ExistEdge(self, u, v):
        return self.edge_matrix[u][v] != self.no_edge_value

    # 算法7-3: 找顶点的第一个邻接点 FirstAdjVert (graph,v)
    def FirstAdjVert(self, v):
        for i in range(self.n_verts):
            if self.edge_matrix[v][i] != self.no_edge_value:
                return i
        return -1

    # 算法7-4: 向图中插入边 InsertEdge(graph, u,v,weight)
    def InsertEdge(self, u, v, weight):
        if self.edge_matrix[u][v] == self.no_edge_value:
            self.edge_matrix[u][v] = weight
            self.m_edges += 1
            if not self.directed:
                self.edge_matrix[v][u] = weight

    # 算法7-5: 从图中删除边 RemoveEdge(graph, u,v)
    def RemoveEdge(self, u, v):
        if self.edge_matrix[u][v] != self.no_edge_value:
            self.edge_matrix[u][v] = self.no_edge_value
            self.m_edges -= 1
            if not self.directed:
                self.edge_matrix[v][u] = self.no_edge_value

    # 算法7-6: 从图中删除顶点及所有邻接于该顶点的边 RemoveVert(graph,v)
    def RemoveVert(self, v):
        if v >= self.n_verts:
            print("错误：待删除的顶点不存在。")
            return
        
        # 删除顶点 v，使用最后一个顶点覆盖它
        self.ver_list[v] = self.ver_list[self.n_verts - 1]
        
        for i in range(self.n_verts):
            if self.edge_matrix[v][i] != self.no_edge_value:
                self.m_edges -= 1
            if self.edge_matrix[i][v] != self.no_edge_value:
                self.m_edges -= 1
        
        # 覆盖行
        for i in range(self.n_verts):
            self.edge_matrix[v][i] = self.edge_matrix[self.n_verts - 1][i]
        
        # 覆盖列
        for i in range(self.n_verts):
            self.edge_matrix[i][v] = self.edge_matrix[i][self.n_verts - 1]
        
        # 覆盖顶点自身
        self.edge_matrix[v][v] = self.edge_matrix[self.n_verts - 1][self.n_verts - 1]
        
        # 清除最后一行和最后一列
        for i in range(self.n_verts):
            self.edge_matrix[self.n_verts - 1][i] = self.no_edge_value
            self.edge_matrix[i][self.n_verts - 1] = self.no_edge_value
        
        self.n_verts -= 1

if __name__ == '__main__':
    kMaxVertex, no_edge_value, directed = [int(i) for i in input().split()[:3]]
    graph = MGraphNode(kMaxVertex, no_edge_value, directed)  # directed 为1的话为有向图，否则为无向图
    vertexList = input().split()[:kMaxVertex]
    for i in range(len(vertexList)):
        graph.ver_list[i] = vertexList[i]
    graph.n_verts = len(vertexList)
    m = int(input())  # 要输入的边的个数
    for i in range(m):
        u, v, weight = [int(x) for x in input().split()[:3]]
        graph.InsertEdge(u, v, weight)
    print("邻接矩阵为：")
    for u in range(graph.n_verts):
        for v in range(graph.n_verts):
            print(graph.edge_matrix[u][v], end=" ")
        print()
    print(f"顶点数 = {graph.NumberOfVerts()}")
    u, v = [int(i) for i in input().split()[:2]]
    print(f"<{u}, {v}> 的存在性 = {graph.ExistEdge(u, v)}")
    u, v = [int(i) for i in input().split()[:2]]
    print(f"<{u}, {v}> 的存在性 = {graph.ExistEdge(u, v)}")
    v = int(input())
    print(f"顶点{v}的第一个邻接点 = {graph.FirstAdjVert(v)}")
    u, v = [int(i) for i in input().split()[:2]]
    graph.RemoveEdge(u, v)
    print(f"<{u}, {v}> 的存在性 = {graph.ExistEdge(u, v)}")
    v = int(input())
    if v < len(graph.ver_list): print(f"待删除的顶点信息为 {graph.ver_list[v]}")
    graph.RemoveVert(v)
    print(f"当前顶点数 = {graph.n_verts}")
    print(f"当前边数 = {graph.m_edges}")
    for v in range(graph.n_verts):
        print(graph.ver_list[v], end="")
    print()
    for u in range(graph.n_verts):
        for v in range(graph.n_verts):
            print(graph.edge_matrix[u][v], end=" ")
        print()
