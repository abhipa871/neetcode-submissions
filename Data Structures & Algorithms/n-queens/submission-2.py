class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        unavoidable = set()
        pos_diag = set()
        neg_diag = set()
        board = [["."] * n for _ in range(n)]
        total = []
        def backtrack(r):
            if r==n:
                total.append(["".join(row) for row in board])
            for c in range(n):
                if c in unavoidable or r-c in pos_diag or r+c in neg_diag:
                    continue
                unavoidable.add(c)
                pos_diag.add(r-c)
                neg_diag.add(r+c)
                board[r][c] = 'Q'
                backtrack(r+1)
                board[r][c] = '.'
                pos_diag.remove(r-c)
                neg_diag.remove(r+c)
                unavoidable.remove(c)

        backtrack(0)        
        return total



