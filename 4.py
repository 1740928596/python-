bihua = {0: 13, 1: 1, 2: 2, 3: 3, 4: 5, 5: 4, 6: 4, 7: 2, 8: 2, 9: 2}
years=[]
months=[]
days=[]

for i in range(0,3):
    if i ==2:
        k = 5
    else:
        k = 10
    for j in range(0,k):
        years.append(bihua[i]+bihua[j])

print("年：",years)
#所有年份


for i in range(0,2):
    if i == 0:
        a = 1
        b = 10
    else:
        a = 0
        b = 3
    for j in range(a,b):
        months.append(bihua[i]+bihua[j])
print("月：",months)
#所有月份


for i in range(0,4):
    if i == 3:
        days.append(16)
        days.append(4)
        break
    if i == 0:
        a = 1
        b = 10
    else:
        a = 0
        b = 10
    for j in range(a,b):
        days.append(bihua[i]+bihua[j])
print("日：",days)
#所有日期

sum = 0
for i in years:
    for j in months:
        if j == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            for k in range(0,30):
                if i+j+days[k] ==35:
                    print("%d+%d+%d = 35" %(i, j, days[k]))
                    sum+=1
        else:
            for k in range(0,31):
                if i+j+days[k] ==35:
                    print("%d+%d+%d = 35" %(i, j, days[k]))
                    sum+=1

print("总数为:",sum)

