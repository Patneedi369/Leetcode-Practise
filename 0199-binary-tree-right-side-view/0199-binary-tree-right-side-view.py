
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        res = []

        while queue:
            ls = []

            for _ in range(len(queue)):
                node = queue.popleft()
                ls.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            res.append(ls[-1])

        return res