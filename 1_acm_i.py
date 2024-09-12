from collections import defaultdict

# 深度优先搜索找到树的直径
def dfs(node, parent, depth):
    global max_depth, farthest_node
    if depth > max_depth:
        max_depth = depth
        farthest_node = node
    for child in tree[node]:
        if child != parent:
            dfs(child, node, depth + 1)

# 计算树的直径长度
def diameter():
    global max_depth, farthest_node
    max_depth = 0
    dfs(1, -1, 0)  # 从任意节点开始深度优先搜索
    max_depth = 0
    dfs(farthest_node, -1, 0)  # 从最远的节点开始深度优先搜索
    return max_depth

# 主函数
def main():
    n = int(input())
    global tree
    tree = defaultdict(list)
    edges = list(map(int, input().split()))
    for i in range(n - 1):
        u, v = i + 2, edges[i]
        tree[u].append(v)
        tree[v].append(u)
    diameter_length = diameter()  # 计算树的直径长度
    # 根据直径长度计算环的期望长度
    numerator = 2 * diameter_length
    denominator = 1
    print(f"{numerator}/{denominator}")

if __name__ == "__main__":
    main()
