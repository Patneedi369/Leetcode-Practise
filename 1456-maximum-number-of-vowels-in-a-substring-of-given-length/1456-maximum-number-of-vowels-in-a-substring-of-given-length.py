class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        flag = 0
        vowels = ('a', 'e', 'i', 'o', 'u')
        for i in range(0,k):
            if s[i] in vowels:
                flag += 1

        maxValue = flag
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                flag -= 1
            if s[i] in vowels:
                flag += 1
            maxValue = max(maxValue, flag)

        return maxValue

