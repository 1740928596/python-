import numpy as np

def creat_(n,m):
    a = np.zeros((n,m),int)
    for j in range(n):
       a[j] = list(map(int,input().split()))
    return a

T = int(input())


for i in range(T):
    n,m,k=map(int,input().split())
    a = creat_(n,m)
    b = creat_(m,k)
    c = np.dot(a,b)
    for j in range(n):
        for l in range(k):
            print(c[j][l],end=" ")
        print()
