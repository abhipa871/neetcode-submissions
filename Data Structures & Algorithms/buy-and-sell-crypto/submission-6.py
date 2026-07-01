class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       left_ptr = 0
       max_diff = 0
       for i in range(1, len(prices)):
         if(prices[i]<prices[left_ptr]):
            left_ptr = i
         max_diff = max(max_diff, prices[i]-prices[left_ptr])
       return max_diff