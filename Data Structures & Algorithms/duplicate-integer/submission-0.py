class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         dict = {}
         for i in range(len(nums)):
            dict[nums[i]] = dict.get(nums[i], 0)+1
            if(dict[nums[i]]>1):
                return True
         return False