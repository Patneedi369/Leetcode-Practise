class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        appeared = set()
        for i in arr:
            if (i*2 in appeared) or (i%2==0 and i//2 in appeared):
                return True
            else:
                appeared.add(i)
        return False