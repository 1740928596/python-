def calculate_M(a, b, c, S):
    def T(M):
        return a + b * M + c * M * M
    
    low, high = 0, S
    while high - low > 1e-7:
        mid = (low + high) / 2
        if mid * T(mid) <= S and T(mid) <= 24:
            low = mid
        else:
            high = mid
    return round(low, 2)

def main():
    N = int(input().strip())
    results = []
    
    for _ in range(N):
        a, b, c, S = map(float, input().strip().split())
        M = calculate_M(a, b, c, S)
        results.append(f"{M:.2f}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
