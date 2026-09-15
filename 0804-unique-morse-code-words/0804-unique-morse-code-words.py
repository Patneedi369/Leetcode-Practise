class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Fixed 'y' at index 24 from ".-.--" to "-.--"
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        
        transformations = set()
        
        for word in words:
            code = "".join(morse[ord(char) - ord('a')] for char in word)
            transformations.add(code)
            
        return len(transformations)