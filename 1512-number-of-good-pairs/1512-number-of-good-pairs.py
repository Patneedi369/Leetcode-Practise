class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = [0]*101
        res = 0
        for i in nums:
            res += freq[i]
            freq[i] += 1
        return res