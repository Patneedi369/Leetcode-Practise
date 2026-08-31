class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        common = set(nums1)&set(nums2)
        a0 = []
        a1 = []
        for i in set(nums1):
            if i not in common:
                a0.append(i)
        for i in set(nums2):
            if i not in common:
                a1.append(i)
        return [a0,a1]