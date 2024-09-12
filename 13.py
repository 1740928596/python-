def is_three(x):
    res = 0
    for i in x:
        res += i
    if res % 3 == 0:
        print("yes",end=" ")
    else:
        print("no",end=" ")


def is_eleven(x):
    res_1 = 0
    res_0 = 0
    for i in range(0, len(x),2):
        res_0 += x[i]
    for i in range(1, len(x),2):
        res_1 += x[i]
    if abs(res_1-res_0) % 11 == 0:
        print("yes")
    else:
        print("no")


n = int(input())
for i in range(n):
    x = list(map(int, input()))
    is_three(x)
    is_eleven(x)
