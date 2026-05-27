class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_ptr = 0
        max_diff = 0
        for right_ptr in range(1, len(prices)):
            if prices[right_ptr] < prices[left_ptr]:
                left_ptr=right_ptr
            else:
                max_diff = max(max_diff, prices[right_ptr] - prices[left_ptr])
        return max_diff    