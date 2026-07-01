class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let left = 0
        let right = height.length-1
        let maxRight = -1
        let maxLeft = -1
        let area =0
        while(left<right)
        {
            if(height[left]<height[right])
            {
                maxLeft = Math.max(maxLeft, height[left])
                area+=maxLeft-height[left]
                left++
            }
            else
            {
                maxRight = Math.max(maxRight, height[right])
                area+=maxRight-height[right]
                right--
            }

        }
        return area;
    }
}
