class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(nums)
        # Size matches len(nums) exactly
        smaller_count = [0] * len(nums)

        # Loop through the entire sorted list length
        for i in range(1, len(nums)):
            if sorted_list[i-1] != sorted_list[i]:
                smaller_count[i] = i
            else:
                smaller_count[i] = smaller_count[i-1]

        result = []
        for num in nums:
            target = num
            low = 0
            high = len(sorted_list) - 1
            index = 0

            while low <= high:
                mid = low + (high - low) // 2
                
                if sorted_list[mid] == target:
                    index = mid
                    break  
                elif sorted_list[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            result.append(smaller_count[index])

        return result