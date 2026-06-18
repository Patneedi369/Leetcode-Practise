class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        commondict = {}
        for letter in s:
            if letter in commondict:
                commondict[letter] += 1
            else:
                commondict[letter] = 1
        for letter in t:
            if letter in commondict:
                commondict[letter] -= 1
            if letter not in commondict or commondict[letter] < 0:
                return False
        return True
        