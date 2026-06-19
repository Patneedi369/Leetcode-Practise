class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        seen_values = set()
        for i, ch in enumerate(s):
            if ch in mapping:
                if t[i] != mapping[ch]:
                    return False
            else:
                if t[i] in seen_values:
                    return False
                mapping[ch] = t[i]
                seen_values.add(t[i])
        return True