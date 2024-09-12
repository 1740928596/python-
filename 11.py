import math

N = 2000 + 10
M = 4000000 + 10
INF = int(1e9 + 10)

def read_input():
    n, m = map(int, input().split())
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(input())
    return n, m, a

def preprocess_sum_matrix(n, m, a):
    sum_matrix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, n + 1):
        for t in range(1, m + 1):
            sum_matrix[t][i] = sum_matrix[t][i - 1]
        sum_matrix[a[i]][i] = sum_matrix[a[i]][i - 1] + 1
    return sum_matrix

def process_queries(sum_matrix, m):
    q = int(input())
    results = []
    for _ in range(q):
        l, r = map(int, input().split())
        ans = 0
        for i in range(1, m + 1):
            if sum_matrix[i][r] - sum_matrix[i][l - 1] > 0:
                ans += 1
        results.append(ans)
    return results

def main():
    n, m, a = read_input()
    sum_matrix = preprocess_sum_matrix(n, m, a)
    results = process_queries(sum_matrix, m)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
