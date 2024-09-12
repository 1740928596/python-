import math
T = int(input())
b = list(map(int, input().split()))

res = 0
for i in range(T):
    if i !=0:
        x=abs(sum(b[0:i])-b[i])
        if x>res:res=x
    if i !=T-1:
        y=abs(sum(b[i+1:T])-b[i])
        if y>res:res=y



print(res)


