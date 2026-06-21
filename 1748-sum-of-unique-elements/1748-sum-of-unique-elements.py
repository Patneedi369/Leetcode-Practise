class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        array = [0]*101
        for num in nums:
            array[num] += 1

        output = 0
        for num in nums:
            if array[num] == 1:
                output += num
        
        return output

