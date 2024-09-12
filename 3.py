def find_longest_increasing_subsequence(arr):
    n = len(arr)
    if n == 0: 
        return []
    
    max_len = 1
    max_start = 0
    current_start = 0
    current_len = 1
    
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_start = current_start
            current_len = 1
            current_start = i
    
    if current_len > max_len:
        max_len = current_len
        max_start = current_start
    
    return arr[max_start:max_start+max_len]

# 读取输入
n = int(input())
arr = list(map(int, input().split()))

# 查找并打印最长连续递增子序列
print(find_longest_increasing_subsequence(arr))


