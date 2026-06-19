class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split()
        if len(pattern) != len(slist):
            return False
        mapping = {}
        seen_values = set()
        for i, ch in enumerate(pattern):
            if ch in mapping:
                if slist[i] != mapping[ch]:
                    return False
            else:
                if slist[i] in seen_values:
                    return False
                mapping[ch] = slist[i]
                seen_values.add(slist[i])
        return True