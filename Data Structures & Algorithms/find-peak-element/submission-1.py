class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        middle = 0

        while middle < len(nums):
            left_bound = None
            if middle - 1 < 0:
                left_bound = float('-inf')
            else:
                left_bound = nums[middle-1]    

            right_bound = None

            if middle + 1 >= len(nums):
                right_bound = float('-inf')
            else:
                right_bound = nums[middle+1]     
            
            if left_bound < nums[middle] > right_bound:
                print()
                return middle

            middle+=1



        