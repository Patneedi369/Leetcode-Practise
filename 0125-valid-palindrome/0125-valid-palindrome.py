class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<right:
            
            if not s[right].isalnum():
                right -= 1
                continue

            if not s[left].isalnum(): 
                left += 1
                continue

            if s[right].lower() != s[left].lower():
                return False

            right -= 1
            left += 1
            
        return True


'''
Without continue:

right becomes 1
Then the same iteration compares s[left] and s[right]

This is error-prone because you've changed one pointer but not restarted the loop.

With continue:

Move the pointer.
Restart the loop.
Compare only after both left and right point to valid alphanumeric characters.
'''