class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        
        # set(word).issubset(allowed_set) checks if all characters in word exist inside allowed_set
        return sum(1 for word in words if set(word).issubset(allowed_set))