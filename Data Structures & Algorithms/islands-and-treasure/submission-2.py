from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r, c):
            steps = 0
            queue = deque([(r, c)])
            visited = {(r, c)}

            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()

                    if grid[row][col] == 0:
                        return steps

                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc

                        if (
                            new_row < 0
                            or new_col < 0
                            or new_row >= ROWS
                            or new_col >= COLS
                            or (new_row, new_col) in visited
                            or grid[new_row][new_col] == -1
                        ):
                            continue

                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

                steps += 1

            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)