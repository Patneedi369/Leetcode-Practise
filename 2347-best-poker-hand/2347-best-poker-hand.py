class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits))==1:
            return "Flush"

        max_freq = max(Counter(ranks).values()) #highest rank count
        if max_freq >= 3:
            return "Three of a Kind"
        elif max_freq == 2:
            return "Pair"
        else:
            return "High Card"
        