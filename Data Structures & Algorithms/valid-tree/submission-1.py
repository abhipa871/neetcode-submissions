class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        queue = deque([(0, -1)])
        visited.add(0)
        while queue:
            node, parent = queue.popleft()
            for neighbor in graph[node]:
        
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return False
        return True if len(visited)==n else False
