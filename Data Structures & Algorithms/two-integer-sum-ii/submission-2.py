class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr_one = 0
        ptr_two = len(numbers)-1
        while ptr_one<ptr_two:
            if numbers[ptr_one]+numbers[ptr_two]>target:
                ptr_two-=1
            elif numbers[ptr_one]+numbers[ptr_two]<target:
                ptr_one+=1
            elif numbers[ptr_one]+numbers[ptr_two]==target:
                return [ptr_one+1, ptr_two+1]