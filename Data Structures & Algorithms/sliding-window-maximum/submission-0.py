class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       max_heap = []
       output = []
       for right_ptr in range(len(nums)):
          heapq.heappush(max_heap, (-nums[right_ptr], right_ptr))
          if right_ptr>= k-1:
            while max_heap[0][1] <=right_ptr-k:
               heapq.heappop(max_heap)
            output.append(-max_heap[0][0])
       return output