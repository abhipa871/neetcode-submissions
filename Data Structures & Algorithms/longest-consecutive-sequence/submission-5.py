class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        print(num_set)
        max_length = 0
        for num in num_set:
            length = 0
            if num-1 not in num_set:
                length =1
                while num+length in num_set:
                    length+=1
                max_length = max(length, max_length)
        return max_length