class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap:
                return [i, hashmap[num]]
            else:
                hashmap[target - num] = i
        return -1