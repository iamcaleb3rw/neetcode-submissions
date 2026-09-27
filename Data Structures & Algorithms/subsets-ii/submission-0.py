class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #On each branch i could choose to includ or not to include the number
        #the base case
        nums.sort()
        res = []
        def backtrack(i, choice):
            if i == len(nums):
                res.append(list(choice))
                return

            choice.append(nums[i])
            backtrack(i+1, choice)
            choice.pop()

            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i+=1

            backtrack(i+1, choice)

        backtrack(0, [])
        return res

        