class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            mid_val = nums[mid]

            if mid_val == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < mid_val:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if mid_val < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1    
        return -1            


        