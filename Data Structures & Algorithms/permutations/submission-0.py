class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, perm = [], []

        def dfs():
            if len(perm) == len(nums):
                ans.append(list(perm))
                return

            for num in nums:
                if num not in perm:
                    perm.append(num)
                    dfs()
                    perm.pop()
        dfs()
        return ans            




        