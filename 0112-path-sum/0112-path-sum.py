class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        remaining = targetSum - root.val

        if not root.left and not root.right:
            if remaining == 0:
                return True

        return (
            self.hasPathSum(root.left, remaining) or 
            self.hasPathSum(root.right, remaining)
        )