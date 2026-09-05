class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = [0]*101
        res = 0
        for i in nums:
            res += freq[i]
            freq[i] += 1
        return res


'''
dry run

Step,Current i,freq[i] before update,res added,Total res,freq[i] after update
1,1,0,+ 0,0,freq[1] = 1
2,2,0,+ 0,0,freq[2] = 1
3,3,0,+ 0,0,freq[3] = 1
4,1,1,+ 1,1,freq[1] = 2
5,1,2,+ 2,3,freq[1] = 3
6,3,1,+ 1,4,freq[3] = 2
'''