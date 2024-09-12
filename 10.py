def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    
    a = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        tmp = int(data[index])
        index += 1
        a[i][tmp] = 1
        for j in range(1, m + 1):
            a[i][j] += a[i - 1][j]
    
    Q = int(data[index])
    index += 1
    results = []
    
    for _ in range(Q):
        l = int(data[index])
        index += 1
        r = int(data[index])
        index += 1
        ans = 0
        for j in range(1, m + 1):
            if a[r][j] > a[l - 1][j]:
                ans += 1
        results.append(ans)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
