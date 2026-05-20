class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        indices = []
        for i in range(len(nums)):
            current = nums[i];
            for j in range(i+1, len(nums)):
                sum = current + nums[j]
                if(sum == target):
                    indices.append(i)
                    indices.append(j)
        return indices            