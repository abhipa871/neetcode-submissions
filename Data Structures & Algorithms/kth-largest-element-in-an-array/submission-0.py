class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, num)
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        print(maxHeap)
        return maxHeap[0]