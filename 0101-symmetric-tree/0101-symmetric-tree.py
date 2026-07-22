class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = collections.deque([root])

        while queue:
            ls = []

            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    ls.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    ls.append(None)

            if ls != ls[::-1]:
                return False

        return True