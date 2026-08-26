class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        for key in sorted(freq.keys(), reverse=True):
            if key==freq[key]:
                return key
        return -1