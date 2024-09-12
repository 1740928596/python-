import math

def count_x(a, b):
        c = a - b
        count = 0
        for i in range(1, int(math.sqrt(c)) + 1):
            if c % i == 0:
                if i > b:
                    count += 1
                if i != c // i and c // i > b:
                    count += 1
        return count

T = int(input())
for _ in range(T):
    a,b=map(int,input().split()) 
    if a != b:
        num_x = count_x(a, b)
        print(num_x)
    else: print("infinity")
    
