class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Transform: target -> +1, others -> -1
        prefix = [0]
        cur = 0
        for x in nums:
            if x == target:
                cur += 1
            else:
                cur -= 1
            prefix.append(cur)

        # Coordinate compression
        vals = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        m = len(vals)
        bit = [0] * (m + 1)

        def update(i):
            while i <= m:
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        ans = 0

        for p in prefix:
            idx = rank[p]
            ans += query(idx - 1)
            update(idx)

        return ans