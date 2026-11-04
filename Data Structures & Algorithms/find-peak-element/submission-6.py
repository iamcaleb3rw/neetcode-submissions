class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #start at left = 0 and right at n-1
        #compute the midpoint
        #check if the midpoint is peak
        #check if left and right are peaks
        #if not look for a greater adjacent, 
        #if the greater adjacent element is in the left subarray, move the right pointer to middle
        #if the greater adjacent element is in the right subarray, move the left pointer to middle
        n = len(nums)
        if n==1:
            return 0
        def isPeak(index):
            if index == 0: 
                return nums[0] > nums[1]
            elif index == n-1:
                return nums[index] > nums[index-1]
            else:
                return nums[index-1] <nums[index] > nums[index+1]
    

        left, right = 0, len(nums) -1

        if isPeak(left):
                return left

        if isPeak(right):
            return right

        if not right:
            return 0

        while left <= right:
            mid = (left + right ) // 2

            if isPeak(mid):
                return mid

                    

            if nums[mid] < nums[mid+1]:
                left = mid
            else:
                right = mid               








        