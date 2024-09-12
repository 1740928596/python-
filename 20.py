class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.cover = [-1] * (n << 2)
        self.sum = [0] * (n << 2)
        self.lsum = [0] * (n << 2)
        self.rsum = [0] * (n << 2)
        self.build(1, n, 1)

    def build(self, l, r, rt):
        self.cover[rt] = -1
        self.sum[rt] = self.lsum[rt] = self.rsum[rt] = r - l + 1
        if l == r:
            return
        m = (l + r) >> 1
        self.build(l, m, rt << 1)
        self.build(m + 1, r, rt << 1 | 1)

    def pushdown(self, rt, length):
        if self.cover[rt] != -1:
            self.cover[rt << 1] = self.cover[rt << 1 | 1] = self.cover[rt]
            self.sum[rt << 1] = self.lsum[rt << 1] = self.rsum[rt << 1] = 0 if self.cover[rt] else length - (length >> 1)
            self.sum[rt << 1 | 1] = self.lsum[rt << 1 | 1] = self.rsum[rt << 1 | 1] = 0 if self.cover[rt] else length >> 1
            self.cover[rt] = -1

    def pushup(self, rt, length):
        self.lsum[rt] = self.lsum[rt << 1]
        self.rsum[rt] = self.rsum[rt << 1 | 1]
        if self.lsum[rt] == length - (length >> 1):
            self.lsum[rt] += self.lsum[rt << 1 | 1]
        if self.rsum[rt] == length >> 1:
            self.rsum[rt] += self.rsum[rt << 1]
        self.sum[rt] = max(self.lsum[rt << 1 | 1] + self.rsum[rt << 1], max(self.sum[rt << 1], self.sum[rt << 1 | 1]))

    def query(self, length, l, r, rt):
        if l == r:
            return 1
        self.pushdown(rt, r - l + 1)
        m = (l + r) >> 1
        if self.sum[rt << 1] >= length:
            return self.query(length, l, m, rt << 1)
        elif self.rsum[rt << 1] + self.lsum[rt << 1 | 1] >= length:
            return m - self.rsum[rt << 1] + 1
        else:
            return self.query(length, m + 1, r, rt << 1 | 1)

    def update(self, L, R, c, l, r, rt):
        if L <= l and r <= R:
            self.lsum[rt] = self.rsum[rt] = self.sum[rt] = 0 if c else r - l + 1
            self.cover[rt] = c
            return
        self.pushdown(rt, r - l + 1)
        m = (l + r) >> 1
        if m >= L:
            self.update(L, R, c, l, m, rt << 1)
        if m < R:
            self.update(L, R, c, m + 1, r, rt << 1 | 1)
        self.pushup(rt, r - l + 1)

def main():
    n, q = map(int, input().split())
    tree = SegmentTree(n)
    for _ in range(q):
        command = list(map(int, input().split()))
        cmd = command[0]
        if cmd == 1:
            a = command[1]
            if tree.sum[1] < a:
                print(0)
            else:
                ans = tree.query(a, 1, n, 1)
                print(ans)
                tree.update(ans, a + ans - 1, 1, 1, n, 1)
        else:
            a, b = command[1], command[2]
            tree.update(a, a + b - 1, 0, 1, n, 1)

if __name__ == "__main__":
    main()
