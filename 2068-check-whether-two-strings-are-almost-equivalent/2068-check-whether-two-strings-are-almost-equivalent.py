class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        lword1 = {}
        for ch in word1:
            lword1[ch] = lword1.get(ch, 0) + 1
        lword2={}
        for ch in word2:
            lword2[ch] = lword2.get(ch, 0) + 1

        for i in range(0,26):
            ch = chr(ord('a')+i)
            c1 = lword1.get(ch,0)
            c2 = lword2.get(ch,0)
            if abs(c1-c2)>3:
                return False
        return True