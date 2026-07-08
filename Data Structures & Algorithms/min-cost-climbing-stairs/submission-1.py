class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def find(i, rem):
            if i in memo:
                return memo[i]
            if rem == 0 or i > n:
                return 0
            cost_i = cost[i]    
            #climb one
            one = cost_i + find(i+1, rem-1)
            #climb two
            two = cost_i + find(i+2, rem-2)

            memo[i] = min(one, two)
            return memo[i]
        return min(find(0, n), find(1, n-1))   

        