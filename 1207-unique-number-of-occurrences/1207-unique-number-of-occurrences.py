class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        collection = {}
        
        for num in arr:
            if num not in collection:
                collection[num] = 1
            else:
                collection[num] += 1
        
        if len(collection) == len(set(collection.values())):
            return True

        return False

            