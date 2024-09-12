n = int(input())
array = list(map(int,input().split(" ")))
m = int(input())
if n <= 0:
    print("%d 未找到。"%m)
if m in array:
    print(int(array.index(m)+1))
else:
    print("%d 未找到。"%m)
