def expected_ranking(n, estimations):
    estimations_with_index = [(estimations[i], i) for i in range(n)]
    estimations_with_index.sort()

    result = [0] * n
    for i in range(n):
        count = 0
        for j in range(n):
            if i != j:
                if estimations_with_index[j][0][1] > estimations_with_index[i][0][0]:
                    count += 1
        result[estimations_with_index[i][1]] = count + 1

    return result

# 读取输入
n = int(input())
estimations = [list(map(float, input().split())) for _ in range(n)]

# 计算期望排名
rankings = expected_ranking(n, estimations)

# 输出期望排名
for rank in rankings:
    print(rank, end=" ")







