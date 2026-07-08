class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def find(n):
            if n in memo:
                return memo[n]
            if n <= 1:
                return 1

            memo[n] = find(n-1) + find(n-2)
            return memo[n]

        return find(n)        
        