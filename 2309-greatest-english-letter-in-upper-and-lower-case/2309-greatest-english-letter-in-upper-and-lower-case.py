class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set(s)
        # Check from 'Z' down to 'A'
        for ch in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
            if ch in seen and ch.lower() in seen:
                return ch
        return ""