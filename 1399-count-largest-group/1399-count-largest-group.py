from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def get_digit_sum(num: int) -> int:
            return sum(int(digit) for digit in str(num))
        
        # Frequency hash map to store count of numbers for each digit sum
        counts = Counter(get_digit_sum(i) for i in range(1, n + 1))
        
        # Find the maximum size (group frequency)
        max_size = max(counts.values())
        
        # Count how many groups have this maximum size
        return sum(1 for size in counts.values() if size == max_size)