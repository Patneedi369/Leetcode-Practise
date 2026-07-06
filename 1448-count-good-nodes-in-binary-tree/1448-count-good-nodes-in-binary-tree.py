
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.count = 0
        def helper(root, maxNum):
            if root.val >= maxNum: self.count += 1
            maxNum = max(maxNum, root.val)
            if root.left: helper(root.left, maxNum)
            if root.right: helper(root.right, maxNum)
            return self.count

        return helper(root, maxNum = -1000000) 

