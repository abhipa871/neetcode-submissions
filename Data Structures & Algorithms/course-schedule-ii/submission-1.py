class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        traversal = []
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course]+=1
        queue = deque()
        for node in range(numCourses):
            if indegree[node]==0:
                queue.append(node)
        processed = 0
        while queue:
            node = queue.popleft()
            traversal.append(node)
            processed+=1
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        return traversal if processed==numCourses else []