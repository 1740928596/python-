inf = float("inf")
str_ = input()
n = int(input())
for _ in range(n):
    start, end, str1, str2 = input().split()
    start = int(start) - 1
    end = int(end)
    copy = str_[start:end]
    # 剪切
    str_ = str_[:start] + str_[end:]


    start1 = 0
    end1 = -1
    while end1 != start1:
        try :
            start1 = str_.index(str1,start1) + len(str1)
            end1 = str_.index(str2, start1)
        except:
            break



    if end1 == start1:
        str_ = str_[:start1] + copy + str_[end1:]
    else:
        str_ = str_ +copy




print(str_)