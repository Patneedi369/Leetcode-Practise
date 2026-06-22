class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i,num in enumerate(nums):
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        
        return [i+1 for i in range(0,len(nums)) if nums[i]>0]
