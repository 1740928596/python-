def creat_(n,m):

    a = []
    for j in range(n):
       a.append(list(map(int,input().split())))
    return a



T = int(input())
for i in range(T):
    n,m,k=map(int,input().split())
    a = creat_(n,m)
    b = creat_(m,k)
    for j in range(n):
        for l in range(k):
                res = 0
                for h in range(m):
                    c = a[j][h]*b[h][l]
                    res+=c
                print(res, end=" ")
        print()