import math

N = 2000 + 10
M = 4000000 + 10
inf = int(1e9) + 10

# Initialize sum and a arrays
sum_arr = [[0] * N for _ in range(N)]
a = [0] * N

def main():
    # Read n and m
    n, m = map(int, input().split())

    # Read the array a
    a[1:n+1] = list(map(int, input().split()))

    # Calculate the sum array
    for i in range(1, n + 1):
        for t in range(1, m + 1):
            sum_arr[t][i] = sum_arr[t][i - 1]
        sum_arr[a[i]][i] = sum_arr[a[i]][i - 1] + 1

    # Read number of queries
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        ans = 0
        for i in range(1, m + 1):
            if sum_arr[i][r] - sum_arr[i][l - 1] > 0:
                ans += 1
        print(ans)

if __name__ == "__main__":
    main()
