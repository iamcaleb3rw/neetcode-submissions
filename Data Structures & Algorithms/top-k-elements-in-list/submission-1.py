class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} #item -> frequency

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

        res= sorted(hashmap, key=lambda x:(-hashmap[x], x))
        result = []

        for i in range(k):
            result.append(res[i])

        return result    
                  