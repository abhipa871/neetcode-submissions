class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS  = len(grid)
        COLS = len(grid[0])
        queue = deque([])
        visited = set()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append((i,j))
                    visited.add((i,j))
        steps = 0
        min = 0
        dist = 0
        def addCell(r, c):
            nonlocal fresh
            if r>=ROWS or c>=COLS or r<0 or c<0 or grid[r][c]==0 or (r,c) in visited:
                return
            visited.add((r, c))
            queue.append((r,c))
            fresh-=1
        while fresh>0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            dist+=1
        return dist if fresh==0 else -1
        