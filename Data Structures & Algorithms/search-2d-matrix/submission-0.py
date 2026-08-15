class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1
        
        while start <= end:
            row = start + ((end - start) // 2)
            if target > matrix[row][-1]:
                start = row + 1
            elif target < matrix[row][0]:
                end = row - 1
            else:
                break
        
        if not (start <= end):
            return False
        
        l, r = 0, len(matrix[row])
        while l <= r:
            mid = l + ((r-l) // 2)
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] == target:
                return True
        
        return False
                



        