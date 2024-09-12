n = int(input())
results=[]
for i in range(0,n):
    m = int(input())
    char1 = input()
    result = 0
    for j in range(0,m):
        char_x=input().split(" ")
        for x in char_x:
            if x ==char1:result+=1
    results.append(result)

for i in results:
    if i == 0:
        print("Do not find\n")
    else:
        print(f"{i}\n")

        