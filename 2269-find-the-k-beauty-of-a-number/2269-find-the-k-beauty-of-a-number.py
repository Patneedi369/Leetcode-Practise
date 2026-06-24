class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        beauty = 0
        for i in range(len(s)+1-k): #range will stop at last index 
            n = int(s[i:i+k])
            if n!=0 and num % n == 0:
                beauty += 1
        return beauty
