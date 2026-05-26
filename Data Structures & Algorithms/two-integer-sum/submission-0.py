class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if(dict.get(target-nums[i], -1)!=-1):
                return [dict[target-nums[i]], i]
            dict[nums[i]] = i
