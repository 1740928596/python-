
list1 = []
for i in range(3):
    a,b,c=map(int,input().split())
    list1.append(a)
    list1.append(b)
    list1.append(c)
    
shuru = list(map(int,input()))

for i in shuru:
    print(list1[i-1],end='')



