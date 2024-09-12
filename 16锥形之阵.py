def calculate_max_soldiers(T, test_cases):
    results = []
    for n in test_cases:
        left, right = 0, n
        while left < right:
            mid = (left + right + 1) // 2
            if mid * (mid + 1) // 2 <= n:
                left = mid
            else:
                right = mid - 1
        results.append(left)
    return results

# 读取输入
T = int(input())
test_cases = [int(input()) for _ in range(T)]

# 计算结果
results = calculate_max_soldiers(T, test_cases)

# 输出结果
for result in results:
    print(result)
