from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_count = sum(1 for c in counts.values() if c == max_freq)

        skeleton_length = (max_freq - 1) * (n + 1) + max_count

        return max(skeleton_length, len(tasks))