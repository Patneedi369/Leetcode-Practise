class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # Replace all non-digit characters with spaces
        cleaned = ''.join(ch if ch.isdigit() else ' ' for ch in word)
        
        # Split by whitespace, normalize numbers by stripping leading zeros (or '0' if all zeros),
        # and store them in a set to count unique values.
        unique_integers = {num.lstrip('0') or '0' for num in cleaned.split()}
        
        return len(unique_integers)