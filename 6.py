import sys
from collections import deque

class Node:
    def __init__(self, name, loc, dir, s):
        self.name = name
        self.loc = loc
        self.dir = dir
        self.s = s

def cmp(a):
    return a.loc

def ini():
    global T
    T = int(input().strip())

def work():
    ith = 1
    global T
    results = []
    while T > 0:
        T -= 1
        dq = deque()
        N, L = map(int, input().strip().split())
        ar = []
        s = []
        for i in range(1, N + 1):
            data = input().strip().split()
            name = data[0]
            loc = int(data[1])
            d = data[2]
            if d == 'R':
                dir = 1
                s_value = L - loc
            else:
                dir = -1
                s_value = loc
            ar.append(Node(name, loc, dir, s_value))
            s.append(s_value)
        
        ar.sort(key=cmp)
        for node in ar:
            dq.append(node)
        s.sort()
        
        results.append(f"Case #{ith}:")
        ith += 1
        for i in range(N):
            result_line = [str(s[i])]
            for j in range(N):
                if ar[j].s == s[i]:
                    if ar[j].dir == 1:
                        result_line.append(dq.pop().name)
                        break
                    else:
                        result_line.append(dq.popleft().name)
                        break
            results.append(" ".join(result_line))
    
    # Output all results at once
    print("\n".join(results))

if __name__ == "__main__":
    ini()
    work()
    # For debugging purposes, the equivalent of the DEBUG part
    # if 'DEBUG' in globals():
    #     nn = int(input())
