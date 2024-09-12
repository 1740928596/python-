import numpy as np

def main():
    while True:
        try:
            T = int(input())
        except EOFError:
            break
        
        for _ in range(T):
            N, M = map(int, input().split())
            a = []
            for _ in range(N):
                row = list(map(int, input().split()))
                a.append(row)
            
            n, m = map(int, input().split())
            b = []
            for _ in range(n):
                row = list(map(int, input().split()))
                b.append(row)
            
            if M != n:
                print("NO")
            else:
                print("YES")
                a = np.array(a)
                b = np.array(b)
                c = np.dot(a, b)
                
                for row in c:
                    print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
