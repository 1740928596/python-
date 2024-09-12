kMaxNum = 1000000000

class G:
    def __init__(self, kMaxV, no_edge_val, directed) -> None:
        self.n = 0
        self.m = 0
        self.e = [[no_edge_val] * kMaxV for _ in range(kMaxV)]
        for i in range(kMaxV):
            self.e[i][i] = 0
        self.v_list = [None] * kMaxV
        self.no_edge_val = no_edge_val
        self.directed = directed

    def exist_edge(self, u, v):
        if u < self.n and v < self.n:
            if u != v and self.e[u][v] != self.no_edge_val:
                return True
        return False

    def insert_edge(self, u, v, weight):
        if not self.exist_edge(u, v):
            self.e[u][v] = weight
            self.m += 1
            if not self.directed:
                self.e[v][u] = weight

    def F(self, p, d):
        n = self.n
        for i in range(n):
            for j in range(n):
                d[i][j] = self.e[i][j]
                if i != j and self.e[i][j] != self.no_edge_val:
                    p[i][j] = i
                else:
                    p[i][j] = -1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][k] != self.no_edge_val and d[k][j] != self.no_edge_val and d[i][k] + d[k][j] < d[i][j]:
                        d[i][j] = d[i][k] + d[k][j]
                        p[i][j] = p[k][j]

if __name__ == '__main__':
    kMaxV = 1000
    p = [[None] * kMaxV for _ in range(kMaxV)]
    d = [[None] * kMaxV for _ in range(kMaxV)]
    no_edge_val = int(input())
    g = G(kMaxV, no_edge_val, True)
    n, m = map(int, input().split()[:2])
    g.n = n
    for _ in range(m):
        u, v, weight = map(int, input().split()[:3])
        g.insert_edge(u, v, weight)
    g.F(p, d)
    print("dist:")
    for u in range(n):
        for v in range(n):
            if d[u][v] == kMaxNum:
                print("1e9", end=" ")
            else:
                print(f"{d[u][v]:>3}", end=" ")
        print()
    print("path:")
    for u in range(n):
        for v in range(n):
            print(f"{p[u][v]:>3}", end=" ")
        print()
