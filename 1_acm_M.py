n, m = (int(x) for x in input().split(" "))
x = ((m - 1) * (n - 1) * (2 * m + 2 * n - 4)) % 998244353
print(x)
