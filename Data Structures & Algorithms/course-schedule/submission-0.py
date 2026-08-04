class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
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
            processed+=1
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        return processed==numCourses