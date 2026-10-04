from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        counts = Counter(num)
        
        for i in range(len(num)):
            expected_count = int(num[i])
            actual_count = counts[str(i)]
            
            if expected_count != actual_count:
                return False
                
        return True