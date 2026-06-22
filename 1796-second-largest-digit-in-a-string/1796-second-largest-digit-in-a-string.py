class Solution:
    def secondHighest(self, s: str) -> int:
        first_largest = -1
        second_largest = -1

        for ch in s:
            if ch.isdigit():
                digit = int(ch)

                if digit > first_largest:
                    second_largest = first_largest
                    first_largest = digit
                
                elif digit < first_largest and digit > second_largest:
                    second_largest = digit

        return second_largest