class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        for i in strs:
            count = [0] * 26
            for ch in i:
                index = ord(ch) - ord('a')
                count[index] += 1

            key = tuple(count)
            if key not in groups:
                groups[key] = []
            groups[key].append(i)

        return list(groups.values())
