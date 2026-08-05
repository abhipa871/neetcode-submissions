class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific = deque()
        atlantic = deque()
        pac = set()
        atl = set()
        for c in range(COLS):
            pacific.append((0, c))
            pac.add((0,c))
            atlantic.append((ROWS - 1, c))
            atl.add((ROWS-1, c))
        for r in range(ROWS):
            if (r,0) not in pac:
                pacific.append((r, 0))
                pac.add((r,0))

            if (r, COLS-1) not in atl:
                atlantic.append((r, COLS - 1))
                atl.add((r,COLS-1))
        
        def bfs(queue, ocean):
            while queue:
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or (nr,nc) in ocean or heights[nr][nc]<heights[r][c]:
                        continue
                    ocean.add((nr,nc))
                    queue.append((nr,nc))
        bfs(pacific, pac)
        bfs(atlantic, atl)
        both = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in pac and (i,j) in atl:
                    both.append([i,j])
        return both


