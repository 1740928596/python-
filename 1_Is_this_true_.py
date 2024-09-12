quan_U = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
P = {0: 0, 1: 1, 2: 1, 3: 1, 4: 0, 5: 1, 6: 0, 7: 1, 8: 0, 9: 1}
Q = {0: 1, 1: 1, 2: 1, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 0}

# 把P，Q分为很多个小P和小Q,以实现多个子区间P和Q,免得反复定义多个P,Q

# 对第一个判断
def test_1():
    a = 0
    b = 2
    while b <= 9:
        positions_1 = 1
        for i in range(a, b):
            if P[i] | Q[i] == 0:
                positions_1 = 0
                break
        positions_2 = 1
        for i in range(a, b):
            for j in range(0, 2):
                if P[i] | Q[j] == 0:
                    positions_2 = 0
                    break
        if positions_1 != positions_2:
            return False
        a += 1
        b += 1
    return True

# 对第二个的判断
def test_2():
    a = 0
    b = 2
    while b <= 9:
        positions_1 = 0
        for i in range(a, b):
            if P[i] & Q[i] == 1:
                positions_1 = 1
                break
        positions_2 = 0
        for i in range(a, b):
            for j in range(0, 2):
                if P[i] & Q[j] == 0:
                    positions_2 = 1
                    break
        if positions_1 != positions_2:
            return False
        a += 1
        b += 1
    return True

# 对第三个的判断
def test_3():
    a = 0
    b = 2
    while b <= 9:
        positions_1 = 1
        for i in range(a, b):
            if (not P[i]) | Q[i] == 0:
                positions_1 = 0
                break
        positions_2 = 1
        for i in range(a, b):
            for j in range(0, 2):
                if (not P[i]) | Q[j] == 0:
                    positions_2 = 0
                    break
        if positions_1 != positions_2:
            return False
        a += 1
        b += 1
    return True

# 对第四个的判断
def test_4():
    a = 0
    b = 2
    while b <= 9:
        positions_1 = 0
        for i in range(a, b):
            if (not P[i]) | Q[i] == 1:
                positions_1 = 1
        positions_2 = 0
        for i in range(a, b):
            for j in range(0, 2):
                if (not P[i]) | Q[j] == 0:
                    positions_2 = 1
        if positions_1 != positions_2:
            return False
        a += 1
        b += 1
    return True

if test_1():
    print("等价")
else:
    print("不等价")

if test_2():
    print("等价")
else:
    print("不等价")

if test_3():
    print("等价")
else:
    print("不等价")

if test_4():
    print("等价")
else:
    print("不等价")