class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high  = 1, max(piles)
        res = max(piles)
        while low<=high:
            mid = low + (high-low)//2
            totalTime = 0
            for i in range(len(piles)):
                totalTime+=math.ceil(piles[i]/mid)
            if totalTime<=h:
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res