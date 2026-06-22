class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}
        for ch in s:
            if ch not in frequency:
                frequency[ch] = 1
            else:
                frequency[ch] += 1
        
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        
        return -1