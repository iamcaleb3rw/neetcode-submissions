class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def find(i):
            if i in memo:
                return memo[i]
            if i >= n:
                return 0

            memo[i] = max(find(i+1), nums[i]+find(i+2))
            return memo[i]

        return find(0)        




        