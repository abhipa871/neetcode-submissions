class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0
        area = 0
        def dfs(r,c):
            if r>=ROWS or c>=COLS or r<0 or c<0 or grid[r][c]==0 or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and grid[i][j] not in visited:
                    old_len = len(visited)
                    dfs(i, j)
                    area = max(area, len(visited)-old_len)
        return area