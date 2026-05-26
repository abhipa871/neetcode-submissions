class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]*len(nums)
        arr2 = [1]*len(nums)
        res = [1]*len(nums)
        arr[0] = arr2[-1]= 1
        for i in range(1, len(nums)):
            arr[i] = nums[i-1]*arr[i-1]
        for i in range(len(nums)-2, -1, -1):
            arr2[i] = nums[i+1] *arr2[i+1]
        for i in range(len(nums)):
            res[i] = arr[i]*arr2[i]
        return res