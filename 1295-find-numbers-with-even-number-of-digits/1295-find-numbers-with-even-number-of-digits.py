class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        op = 0
        for num in nums:
            if num == 0:
                count = 1
            else:
                count = 0
            while num>0:
                num = num//10
                count += 1
            if count%2==0:
                op += 1
        return op