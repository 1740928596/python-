def main():

    n, m = map(int, input().split(" "))
    array = list(map(int, input().split(" ")))
    
    a = [[0] * (m + 1) for _ in range(n + 3)]
    
    for i in range(1, n + 1):
        tmp = int(array[i-1])
        a[i][tmp] = 1
        for j in range(1, m + 1):
            a[i][j] += a[i - 1][j]
    
    results = []
    
    Q = int(input())
    for _ in range(Q):

        l,r=map(int, input().split(" "))

        ans = 0
        for j in range(1, m + 1):
            if a[r][j] > a[l - 1][j]:
                ans += 1
        results.append(ans)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

