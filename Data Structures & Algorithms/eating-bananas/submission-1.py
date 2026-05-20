class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles) + 1
        trials = range(1, n)
        res = trials[-1]

        def tryK(rate):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/rate)
            return hours

        left, right = 0, len(trials) - 1

        while left <= right:
            mid = left + (right -left)//2

            trial = tryK(trials[mid])

            if trial > h:
                left = mid + 1
            else:
                res = min(res, trials[mid])
                right = mid -1
        return res        



                    
                



        