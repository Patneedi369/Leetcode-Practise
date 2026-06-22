class Solution:
    #this approach is only for sorted input
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Imagine the interviewer gave them to us sorted, or we sort them:
        nums1.sort()
        nums2.sort()
        
        p1, p2 = 0, 0
        res = []
        
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1  # Advance both together on a match!
            elif nums1[p1] < nums2[p2]:
                p1 += 1  # nums1 element is too small, move it forward
            else:
                p2 += 1  # nums2 element is too small, move it forward
                
        return res