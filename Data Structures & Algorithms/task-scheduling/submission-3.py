class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0
        while maxHeap or queue:
            time+=1
            if maxHeap:
                val = heapq.heappop(maxHeap)
                val+=1
                if val<0:
                    queue.append((val, time+n))
            else:
                time = queue[0][1]
            if queue and queue[0][1]==time:
               val, _ = queue.popleft()
               heapq.heappush(maxHeap,val)
        return time
