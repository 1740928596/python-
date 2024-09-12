t = 0
i = 0
list1 = []
while True:
 
    str = input()
    if str==".":
        break
    i+=1
    try:
        str.index("chi1 huo3 guo1")
        t+=1
        list1.append(i)
    except:
        continue
if t!=0:
    print(i)
    print(list1[0],t)

else:
    print(i)
    print("-_-#")



