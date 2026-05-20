class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def binarySearch(target, arr):
            l, r = 0, len(arr) -1
            while l <=r:
                m = (l+r)//2
                if target > arr[m]:
                    l = m+1
                elif target < arr[m]:
                    r = m-1
                else:
                    return True
            return False         

        for i in range(m):
            arr = matrix[i]
            if binarySearch(target, arr):
                return True

        return False        


        