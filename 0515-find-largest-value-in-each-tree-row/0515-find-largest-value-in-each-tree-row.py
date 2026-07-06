
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        res = []

        while queue:
            row_max = float("-inf")
            
            for _ in range(len(queue)):
                node = queue.popleft()
                row_max = max(row_max, node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(row_max)
            
        return res