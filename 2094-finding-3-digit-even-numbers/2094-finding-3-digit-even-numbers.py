from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        # Count frequencies of digits in the input array
        freq = Counter(digits)
        ans = []
        
        # Check all possible 3-digit even numbers
        for num in range(100, 1000, 2):
            # Extract digits of the current number
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            # Count required frequencies for the digits of num
            needed = Counter([d1, d2, d3])
            
            # Check if input digits can form 'num'
            if all(freq[digit] >= count for digit, count in needed.items()):
                ans.append(num)
                
        return ans