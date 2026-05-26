class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)
        list = []
        for n in nums:
            dict[n]+=1
        for i in range(k):
            f = max(dict, key = dict.get)
            list.append(f)
            dict.pop(f)
        return list
            
        

