class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) -1
        n = len(matrix[0]) - 1

        def binarySearch(row, target):
            l,r = 0, len(row) - 1
            while l <= r:
                m = l+(r-l)//2
                if target > row[m]:
                    l = m+1
                elif target < row[m]:
                    r = m-1
                else:
                    return True
            return False                

        while left <= right:
            m = left + (right-left) // 2

            if matrix[m][0] <= target <= matrix[m][n]:
                return binarySearch(matrix[m], target)
            elif target > matrix[m][n]:
                left = m+1
            else:
                right = m-1
        return False                
        