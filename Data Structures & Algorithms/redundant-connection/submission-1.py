from collections import deque
from typing import List

class Solution:
    def findRedundantConnection(
        self,
        edges: List[List[int]]
    ) -> List[int]:
        graph = [[] for _ in range(len(edges) + 1)]

        def connected(start, target):
            queue = deque([start])
            visited = {start}

            while queue:
                node = queue.popleft()

                if node == target:
                    return True

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return False

        for a, b in edges:
            # If a and b are already connected,
            # adding this edge creates a cycle.
            if connected(a, b):
                return [a, b]

            graph[a].append(b)
            graph[b].append(a)

        return []