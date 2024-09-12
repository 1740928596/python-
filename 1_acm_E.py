def jud(n, array, a0, A, B, C, P):
    array[0] = a0
    for i in range(1, n + 1):
        array[i] = (A * array[i - 1] * array[i - 1] + B * array[i - 1] + C) % P
        for j in range(i - 1, -1, -1):
            if array[j] == array[i]:
                return True
    return False

T = int(input())
result = []
for _ in range(T):
    n, a0, A, B, C, P = map(int, input().split())
    array = [0] * (n + 1)
    if jud(n, array, a0, A, B, C, P):
        result.append("Repetitive")
    else:
        result.append("Different")

for res in result:
    print(res)
