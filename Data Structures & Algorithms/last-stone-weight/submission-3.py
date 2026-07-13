class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            heapq.heappush(stones, second-first)
        return -stones[-1]

