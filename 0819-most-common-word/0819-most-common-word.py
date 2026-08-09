import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        
        # Build frequency dictionary directly for non-banned words
        freq = {}
        for word in words:
            if word not in banned_set:
                freq[word] = freq.get(word, 0) + 1
                
        # Find and return the word with the maximum frequency
        return max(freq, key=freq.get)