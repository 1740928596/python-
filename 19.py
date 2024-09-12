n = int(input())
dian = []
score = []
for i in range(n):
    list1 = list(map(int, (input().split())))
    dian.append(list1[0])
    score.append(list1[1])

for i in range(n):
    if 90 <= score[i] <= 100:
        score[i] = 4
    elif 80 <= score[i] < 90:
        score[i] = 3
    elif 70 <= score[i] < 80:
        score[i] = 2
    elif 60 <= score[i] < 70:
        score[i] = 1
    else:
        score[i] = 0
res1 = 0
for i in range(n):
    res1+=dian[i]*score[i]

print(f"{res1/(sum(dian)):.2f}")

