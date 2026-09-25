class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #maintain a frquency hashmap, if an element is part of a successful combination, decrease the frequency
        #on each recursive run, checking if an element has frquency in hashmap becomes a constraint
        #if the sum(choice) == target: we found a combiantion that is valid
        #we can choose to include or not to include an element
        #we use the index i as our recursive state
        res = []
        candidates.sort()

        def backtrack(idx, choice, total):
            if total == target:
                res.append(list(choice))
                return

            if idx >= len(candidates) or total > target:
                return    

            choice.append(candidates[idx])
            backtrack(idx+1, choice, total+candidates[idx])
            choice.pop()

            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx+=1
            backtrack(idx+1, choice, total)
        backtrack(0, [], 0)
        return res        


        