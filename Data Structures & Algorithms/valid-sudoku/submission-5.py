class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                prev_c = len(col[c])
                prev_r = len(row[r])
                prev_square = len(squares[(r//3, c//3)])
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
                if(len(col[c])==prev_c or len(row[r])==prev_r or len(squares[(r//3, c//3)])==prev_square):
                    return False
        return True