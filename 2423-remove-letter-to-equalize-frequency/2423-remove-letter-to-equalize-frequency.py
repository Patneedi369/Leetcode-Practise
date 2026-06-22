class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = {}

        # Count frequency of each character
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        # Try removing one occurrence of each unique character
        for ch in freq:
            freq[ch] -= 1

            # Collect frequencies of remaining characters
            remaining = [count for count in freq.values() if count > 0]

            # If all remaining frequencies are equal
            if len(set(remaining)) <= 1:
                return True

            # Restore the frequency
            freq[ch] += 1

        return False