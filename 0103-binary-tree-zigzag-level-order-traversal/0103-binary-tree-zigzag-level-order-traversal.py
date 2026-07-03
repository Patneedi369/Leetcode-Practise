
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            
            if len(res)%2==0:
                res.append(ls)
            else:
                ls.reverse()
                res.append(ls)

        return res