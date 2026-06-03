class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_k = high
        while low<=high:
            mid  = low + (high-low)//2
            total_time = 0
            for i in range(len(piles)):
                total_time+=math.ceil(piles[i]/mid)
            print(total_time)
            if total_time<=h:
                min_k = mid
                high = mid-1
            else:
                low = mid+1
        return min_k