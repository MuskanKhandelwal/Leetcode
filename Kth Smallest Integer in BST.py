Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, res):
            if not node:
                return 
            res.append(node.val)
            left = dfs(node.left,res)
            right = dfs(node.right,res)
            return res

        res2=dfs(root,res=[])
        print(sorted(res2))
        res2=sorted(res2)
        return res2[k-1]
