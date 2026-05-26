class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]        
        num_groups = {}
        for num in nums:
            num_groups[num] = 1+num_groups.get(num, 0)
        for num, freq in num_groups.items():
            buckets[freq-1].append(num)
        result = []
        for i in range(len(nums)-1, -1, -1):
            if buckets[i]:
                result.extend(buckets[i])
            if len(result)>=k:
                return result[:k]
