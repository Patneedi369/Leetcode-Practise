class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dictionary = {}
        for i,val in enumerate(list1):
            dictionary[val] = i
        
        res = []
        min_index = float('inf')
        for j,val in enumerate(list2):
            if val in dictionary:
                index = j + dictionary[val]
                if index < min_index:
                    min_index = index
                    res = [val]
                elif index == min_index:
                    res.append(val)
                  
        return res