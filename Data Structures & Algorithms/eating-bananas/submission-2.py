
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        speed = 0
        while low<=high:
            mid = low + (high-low)//2
            totalTime = 0

            for i in range(len(piles)):
                totalTime+=math.ceil(float(piles[i])/mid)
            if totalTime<=h:
                speed = mid
                high = mid-1
            else:
                low = mid+1

        return speed
                
