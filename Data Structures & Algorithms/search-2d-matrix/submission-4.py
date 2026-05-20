class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])

        #finding the correct row
        top, bottom = 0, M -1
        while top <= bottom:
            mid = top + (bottom-top) // 2
            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bottom = mid-1
            else:
                break
        if top > bottom:
            return False

        row = matrix[mid]

        l, r = 0, N -1

        while l <= r:
            mid = l + (r - l) // 2
            if target > row[mid]:
                l = mid + 1
            elif target < row[mid]:
                r = mid - 1
            else:
                return True

        return False                                  

        