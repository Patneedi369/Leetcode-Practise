class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        if len(s) < 3:
            return 0
            
        dic = {}
        for i in range(3):
            dic[s[i]] = dic.get(s[i], 0) + 1

        count = 1 if len(dic) ==3 else 0
        for i in range(3, len(s)):
            dic[s[i-3]] -= 1
            if dic[s[i-3]]==0:
                del dic[s[i-3]]

            dic[s[i]] = dic.get(s[i], 0) + 1

            if len(dic)==3:
                count += 1
        
        return count
