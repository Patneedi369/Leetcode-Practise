class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = Counter(arr1)
        res = []

        for i in arr2:
            if i in counts:
                res.extend([i]*counts[i])
                del counts[i]
        
        for i in sorted(counts.keys()):
            res.extend([i]*counts[i])
        
        return res
        