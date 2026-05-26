class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)
        matches = []
        for num in nums:
            table[num]+=1
        freq = [[] for i in range(len(nums)+1)]
        for num, count in table.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq)-1, 0, -1):
            res.extend(freq[i])
            if(len(res)==k):
                return res