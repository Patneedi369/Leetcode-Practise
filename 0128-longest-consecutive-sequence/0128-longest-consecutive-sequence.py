class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        collection = set(nums)
        max_count = 0

        for num in collection:
            # Start of a sequence
            if num - 1 not in collection:
                current = num
                count = 1

                while current + 1 in collection:
                    current += 1
                    count += 1

                max_count = max(max_count, count)

        return max_count