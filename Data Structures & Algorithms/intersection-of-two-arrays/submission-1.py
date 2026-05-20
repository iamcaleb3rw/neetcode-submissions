class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection=[]
        hashset = set()
        for i in nums1:
            hashset.add(i)
        for j in nums2:
            if j in hashset and j not in intersection:
                intersection.append(j)
        return intersection        
