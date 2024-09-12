import numpy as np

def parse_graph_data(file_path):
    """
    从文件中解析数据。
    :param file_path: 文件的路径。
    :return: 图的字典表示，其中键是节点，值是指向的节点集合。
    """
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('#') and line.strip():  # 忽略注释行和空行
                from_node, to_node = map(int, line.split())  # 分割行数据为起始和终止节点
                if from_node in graph:
                    graph[from_node].add(to_node)  # 添加到现有的连接集合中
                else:
                    graph[from_node] = {to_node}  # 创建新的连接集合
                if to_node not in graph:
                    graph[to_node] = set()  # 确保每个节点都在图中
    return graph

def matrix_page_rank(graph, alpha=0.85, k=24, tolerance=1e-6):
    """
    使用矩阵运算计算PageRank。
    :param graph: 图的字典表示。
    :param alpha: 阻尼因子。
    :param k: 最大迭代次数。此处为24次
    :param tolerance: 收敛容忍度。
    :return: 每个节点的PageRank值组成的向量。
    """
    n = len(graph)  # 节点总数
    
    # 初始化邻接矩阵
    M = np.zeros((n, n))
    for j in graph:
        if graph[j]:  # 检查节点j是否有出链
            for i in graph[j]:
                M[i, j] = 1 / len(graph[j])  # 设置转移概率
    
    # 处理没有出链的悬挂节点
    dangling_nodes = np.zeros(n)
    for j in range(n):
        if sum(M[:, j]) == 0:
            dangling_nodes[j] = 1 / n
    
    # 初始化PageRank向量
    p = np.ones(n) / n
    
    # 通过迭代计算PageRank
    for iteration in range(k):
        dangling_weight = np.dot(dangling_nodes, p)  # 计算悬挂节点贡献
        
        # 计算新的PageRank值
        new_p = alpha * (np.dot(M, p) + dangling_weight) + (1 - alpha) / n
        
        # 检查收敛性
        if np.linalg.norm(new_p - p, 1) < tolerance:
            break
        p = new_p
    
    return p

def main(file_path):
    """
    主函数，处理文件路径，计算并打印PageRank。
    :param file_path: 图数据文件的路径。
    """
    graph = parse_graph_data(file_path)  # 解析图数据
    page_ranks = matrix_page_rank(graph)  # 计算PageRank
    sorted_indices = np.argsort(-page_ranks)  # 对PageRank结果进行降序排序
    
    # 打印排序后的PageRank值
    for index in sorted_indices:
        print(f'node_id: {index}  value: [{page_ranks[index]}]')

if __name__ == "__main__":
    main('mini-web-Google.txt')
