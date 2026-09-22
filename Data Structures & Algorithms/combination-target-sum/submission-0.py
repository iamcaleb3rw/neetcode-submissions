class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        choice = []

        #sort the array
        #if the last element is greater than the target no solution
        #recursion function accepts a dfs(total)
        #on each call the sum becomes total + choice we appended
        #if the total equals the target append to result and return
        #otherwise add the current number and remove it
        #add the next number and remove it 
        def dfs(i, total):
            if total == target:
                res.append(list(choice))
                return

            if i >= len(nums) or total > target:
                return    

            choice.append(nums[i])
            dfs(i, total+nums[i])
            
            choice.pop()
            dfs(i+1, total)
        dfs(0, 0)
        return res    

