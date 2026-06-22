class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = set()
        destinys = set()
        for i in range(len(paths)):
            starts.add(paths[i][0])
            destinys.add(paths[i][1])
        return (destinys - starts).pop()

