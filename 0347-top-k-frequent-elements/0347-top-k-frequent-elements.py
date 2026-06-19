class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        collection = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for i, num in enumerate(nums):
            if num in collection:
                collection[num] += 1
            else:
                collection[num] = 1
        
        for num in collection:
            buckets[collection[num]].append(num)
        
        result = []

        # Step backward from the maximum possible frequency down to 0
        for freq in range(len(buckets) - 1, -1, -1):
            for num in buckets[freq]:
                result.append(num)
                
                # The moment we collected the 'k' most frequent items, exit early!
                if len(result) == k:
                    return result
                    
        return result