class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_seen = {}
        max_tracker = diff = -1

        for i, ch in enumerate(s):
            if ch not in first_seen:
                first_seen[ch] = i
            else:
                diff = i - first_seen[ch] - 1
                max_tracker = max(diff, max_tracker)
        
        return max_tracker