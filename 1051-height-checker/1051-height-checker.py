class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        frequency = [0]*101
        count = 0
        for num in heights:
            frequency[num] += 1
        trace = 0
        for i in range(0,101):
            while frequency[i]>0:
                if heights[trace]!=i:
                    count += 1
                trace += 1
                frequency[i] -= 1
        return count