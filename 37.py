str = input()
while True:
    str1 = input()
    if str1 == "-1":
        break
    if len(str1) != len(str):
        print("No")
        continue
    k=0
    for i in range(len(str)):
        if str[i] != str1[i]:
            if abs(int(str[i]) - int(str1[i])) ==1:
                k += 1
            else:
                k = 2
        if k > 1:
            print("No")
            break

    if k <= 1:
        print("Yes")
