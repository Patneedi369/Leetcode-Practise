class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # Step 1: Map each character to its index in the alien alphabet
        order_map = {char: i for i, char in enumerate(order)}
        
        # Step 2: Compare adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            for j in range(len(w1)):
                # If w1 is longer than w2 and w2 is a prefix of w1 (e.g., "apple" vs "app")
                if j >= len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    # If characters differ, check their relative alien rank
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    # Proper order established for this pair, move to the next pair
                    break
                    
        return True