class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        words = text.split()
        op = 0
        for word in words:
            flag = len(word)
            for ch in word:
                if flag != len(word):
                    break
                if ch in broken:
                    flag -= 1
            if flag == len(word):
                op += 1
        return op
            
                