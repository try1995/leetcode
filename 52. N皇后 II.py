class Solution:
    # index对应行，value对应列
    col = []
    num = 0

    # r对应行， c对应列
    def check(self, c, r):
        for i in range(r):
            if self.col[i] == c or abs(i - r) == abs(self.col[i] - c):
                return False
        return True

    def totalNQueens(self, n: int) -> int:
        self.col = [0 for _ in range(20)]
        self.num = 0

        # 一行一行放置
        def DFS(r):
            if r == n:
                self.num += 1
                return
            for c in range(n):
                if self.check(c, r):
                    self.col[r] = c
                    DFS(r + 1)

        DFS(0)
        return self.num