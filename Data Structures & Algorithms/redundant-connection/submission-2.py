from collections import deque
from typing import List

class Solution:
    def findRedundantConnection(
        self,
        edges: List[List[int]]
    ) -> List[int]:
        graph = [[] for _ in range(len(edges) + 1)]
        indegree = [0]*(len(edges)+1)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a]+=1
            indegree[b]+=1
        q = deque()
        for i in range(1, len(edges)+1):
          if indegree[i]==1:
            q.append(i)
        while q:
            node = q.popleft()
            indegree[node]-=1
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==1:
                    q.append(neighbor)
        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        return []