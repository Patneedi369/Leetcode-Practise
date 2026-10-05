class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        result = [words[0]]
        
        for i in range(1, len(words)):
            # If the sorted characters of the current word match the sorted characters
            # of the last appended word, they are anagrams, so we skip it.
            if sorted(words[i]) != sorted(result[-1]):
                result.append(words[i])
                
        return result