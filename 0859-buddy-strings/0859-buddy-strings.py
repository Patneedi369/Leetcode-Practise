class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        # Case 1: s and goal are equal
        if s == goal:
            # Need at least one duplicate character to swap with itself
            return len(set(s)) < len(s)
        
        # Case 2: s and goal are different
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        
        # Exactly 2 differences, and swapping them aligns the strings
        return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]