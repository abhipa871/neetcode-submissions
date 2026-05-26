class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        for i in range(len(nums)):
            if(sum.get(target-nums[i]) is not None and sum.get(target-nums[i])!=i):
                return [sum.get(target-nums[i]), i]
            sum[nums[i]] = i

        return []