dir = {}
M,N = map(int,input().split())
for i in range(M):
    key,level = input().split()
    dir[key] = level

for i in range(N):
    list1 = []
    str = input()
    s = "D"
    for key in dir:
        if str=='':
            break
        try:
            a = str.index(key)
            list1.append(dir[key])
            str = str[:a]+str[a+len(key):]
        except:
            continue


    if len(list1)==2:
        print(list1[0]+list1[1])
    elif len(list1)==1 and str=='':
        print(list1[0])
    else:
        print(s)


