class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let left_ptr = 0
        let max_diff = 0
        for(let i =1; i<prices.length; i++)
        {
            if(prices[i]<prices[left_ptr])
            {
                left_ptr = i
            }
            max_diff = Math.max(max_diff, prices[i]-prices[left_ptr])
        }
        return max_diff
    }
}
