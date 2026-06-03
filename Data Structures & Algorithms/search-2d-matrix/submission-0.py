class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COLS = len(matrix[0])
        nums = matrix
        low = 0
        high = len(matrix)*len(matrix[0])-1
        while low<=high:
            mid = low + (high-low)//2
            row, col = mid//COLS, mid % COLS
            if nums[row][col] == target:
                return True
            elif target > nums[row][col]:
                low = mid + 1
            elif target < nums[row][col]:
                high = mid - 1
        return False