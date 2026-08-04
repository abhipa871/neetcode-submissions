class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
    
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        count=0
        for start in range(n):
            if start in visited: 
                continue
            queue = deque([(start, -1)])
            visited.add(start)
            while queue:
                node, parent = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, node))
            count+=1
        return count