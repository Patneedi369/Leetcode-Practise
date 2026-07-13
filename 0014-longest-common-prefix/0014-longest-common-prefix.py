class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # If the input list is empty, return an empty string
        if not strs:
            return ""
        
        # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Compare this character with the same index in all other strings
            for string in strs[1:]:
                # Check if we reached the end of the current string
                # or if the characters do not match
                if i == len(string) or string[i] != char:
                    return strs[0][:i]
                    
        return strs[0]
