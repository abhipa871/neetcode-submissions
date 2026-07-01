class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let low = 0;
        let high = Math.max(...piles) 
        console.log(high)
        while (low<=high)
        {
            let mid = low + Math.trunc((high-low)/2)

            let totalTime = piles.reduce((accum, current)=>accum+Math.ceil(current/mid), 0);
            if (totalTime <=h)
            {
                high = mid-1
            }
            else
            {
                low = mid+1
            }
        }
        return low;
    }
}
