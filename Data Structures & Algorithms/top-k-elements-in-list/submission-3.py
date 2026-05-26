class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(int)
        for num in nums:
            dictionary[num]+=1
        frequency = defaultdict(list)
        for key, value in dictionary.items():
            frequency[value].append(key)
        print(frequency.items())
        max_count = max(dictionary.values())
        res = []
        for i in range(max_count, 0, -1):
            if i in frequency:                 
                for num in frequency[i]:
                    res.append(num)
                    if len(res) == k:
                        return res