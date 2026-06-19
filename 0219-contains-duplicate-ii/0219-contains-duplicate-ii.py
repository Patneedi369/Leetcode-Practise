class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastseen = {}
        for i,num in enumerate(nums):
            if num in lastseen:
                if i - lastseen[num] <= k:
                    return True
            lastseen[num] = i
        return False