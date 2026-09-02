class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        n = len(s)
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                char_set = set(sub)
                if all(c.swapcase() in char_set for c in sub):
                    if len(sub) > len(ans):
                        ans = sub
                        
        return ans