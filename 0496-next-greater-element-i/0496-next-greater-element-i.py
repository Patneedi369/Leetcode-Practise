class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []
        ans = []

        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                mapping[smaller] = num
            
            stack.append(num)

        for element in nums1:
            if element in mapping:
                ans.append(mapping[element])
            else:
                ans.append(-1)
            
        return ans