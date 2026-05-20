class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res=[]
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] +=1
        sortedmap = sorted(hashmap.items(), key=lambda item:item[1], reverse=True)
        for i in range(k):
            res.append(sortedmap[i][0])
        return res                
        