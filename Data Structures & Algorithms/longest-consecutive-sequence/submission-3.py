class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count=0
        length = 0
        print(num_set)
        for num in num_set:
            if num-1 not in num_set:
                count = 1
                while (num+count) in num_set:
                    count+=1
                length = max(count, length)
        return length