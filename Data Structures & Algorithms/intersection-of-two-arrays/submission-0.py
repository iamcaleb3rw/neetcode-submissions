class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for i in range(len(nums1)):
            currentInt = nums1[i]
            for j in range(len(nums2)):
                if currentInt == nums2[j] and currentInt not in intersection:
                    intersection.append(currentInt)
        return intersection        