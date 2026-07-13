class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        counts = Counter(tasks)
        store = [-count for count in counts.values()]
        heapq.heapify(store)

        queue = deque()  # (remaining_count, available_time)

        while store or queue:
            time += 1

            # Execute a task if one is available
            if store:
                val = heapq.heappop(store)
                val += 1  # -3 -> -2 because one occurrence was completed

                if val < 0:
                    queue.append((val, time + n))

            # Move task back to heap once cooldown is over
            if queue and queue[0][1] == time:
                val, _ = queue.popleft()
                heapq.heappush(store, val)

        return time