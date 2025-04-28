Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]

        def dfs(root):
            if not root:
                return 0
            leftm=dfs(root.left)
            rightm=dfs(root.right)
            leftm = max(leftm, 0)
            rightm = max(rightm, 0)
            res[0]=max(res[0],root.val+leftm+rightm)
            return root.val+max(leftm,rightm)
        dfs(root)
        return res[0]
