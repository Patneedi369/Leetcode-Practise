class Solution:
    def sortString(self, s: str) -> str:
        # Count frequency of each lowercase English letter
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        result = []
        total_chars = len(s)
        
        while len(result) < total_chars:
            # 1. Sweep left-to-right (increasing order: 'a' to 'z')
            for i in range(26):
                if count[i] > 0:
                    result.append(chr(ord('a') + i))
                    count[i] -= 1
            
            # 2. Sweep right-to-left (decreasing order: 'z' to 'a')
            for i in range(25, -1, -1):
                if count[i] > 0:
                    result.append(chr(ord('a') + i))
                    count[i] -= 1
                    
        return "".join(result)