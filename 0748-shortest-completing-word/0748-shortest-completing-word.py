class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        frequency = Counter(ch.lower() for ch in licensePlate if ch.isalpha())

        shortest_word = "0"*1000
        
        for word in words:
            dup_freq = frequency.copy()
            for ch in word:
                if ch.lower() in dup_freq:
                    dup_freq[ch.lower()]-=1
                    if dup_freq[ch.lower()] == 0:
                        del dup_freq[ch.lower()]
            if not dup_freq:
                if len(word) < len(shortest_word):
                    shortest_word = word
        return shortest_word