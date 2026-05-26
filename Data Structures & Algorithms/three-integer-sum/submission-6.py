class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       nums.sort()
       print(nums)
       ptr_one = 0
       ptr_two = len(nums)-1
       close = set()

       for i in range(len(nums)): 
            ptr_one = i+1
            ptr_two = len(nums)-1
            while ptr_one<ptr_two:
                if nums[i] + nums[ptr_one] + nums[ptr_two] > 0:
                    ptr_two-=1
                elif nums[i] + nums[ptr_one] + nums[ptr_two] < 0:
                    ptr_one+=1
                else:
                    close.add(tuple([nums[i], nums[ptr_one], nums[ptr_two]]))
                    ptr_one+=1
                    ptr_two-=1
       return list(close) 
