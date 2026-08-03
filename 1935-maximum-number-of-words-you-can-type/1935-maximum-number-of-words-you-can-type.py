class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        words = text.split()
        
        count = 0
        for word in words:
            # If NONE of the characters in the word are broken, increment count
            if not any(ch in broken for ch in word):
                count += 1
                
        return count