class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numbers:
                return [numbers[diff], i]
            numbers[n] = i