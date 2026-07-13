class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*stone for stone in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first = -1*heapq.heappop(stones)
            second = -1*heapq.heappop(stones)
            heapq.heappush(stones, second-first)
        return stones[-1]*-1

