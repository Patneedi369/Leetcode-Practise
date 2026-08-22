class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)

        digit_sum = sum(int(d) for d in s)
        digit_product = 1
        for d in s:
            digit_product *= int(d) 

        return n%(digit_sum + digit_product)==0