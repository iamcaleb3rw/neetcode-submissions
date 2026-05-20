class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_capacity = max(weights)
        max_capacity = sum(weights)
        res = max_capacity

        def check(mid, days):
            trav = 0
            d = 1
            for weight in weights:
                if trav + weight <= mid:
                   trav += weight
                   continue
                trav = weight   
                d +=1    

            return d       


        l, r  = min_capacity, max_capacity

        while l <=r:
            mid = l+(r-l)//2
            if check(mid,days) > days:
                l = mid + 1
            else: 
                res = min(res, mid) 
                r = mid - 1

        return res        


        


        