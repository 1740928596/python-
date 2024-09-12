T = int(input())
if T == 1:
    print(0)
    exit()
list1 = list(map(int,input().split()))
list2 = sorted(list1)
if list2!=list1:
    print(T)
else:
    print(0)