class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left_ptr, right_ptr = 0,0
        q = deque()
        out = []
        while right_ptr<len(nums):
           while q and nums[q[-1]]<nums[right_ptr]:
              q.pop()
           q.append(right_ptr)
           if left_ptr>q[0]:
             q.popleft()
           if right_ptr+1>=k:
                out.append(nums[q[0]])
                left_ptr += 1

           right_ptr+=1
        return out
           