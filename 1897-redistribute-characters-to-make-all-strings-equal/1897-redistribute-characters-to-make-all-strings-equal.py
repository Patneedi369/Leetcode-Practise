class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        n = len(words)
        counts = Counter("".join(words))
        return all(count % n == 0 for count in counts.values())