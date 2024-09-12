def main():
    t = int(input().strip())
    num = 1
    while t > 0:
        t -= 1
        res = 0
        n = int(input().strip())
        numbers = list(map(int, input().strip().split()))
        for i in range(1, n + 1):
            a = numbers[i - 1]
            if i % 6 == 0 or i % 6 == 2 or i % 6 == 5:
                res ^= a
        if res:
            print(f"Case {num}: Alice")
        else:
            print(f"Case {num}: Bob")
        num += 1

if __name__ == "__main__":
    main()
