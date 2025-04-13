Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftHeight=self.maxheight(root.left)
        rightHeight=self.maxheight(root.right)
        diameter = abs(leftHeight - rightHeight )
        if(diameter>1):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def maxheight(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0
        leftheight=self.maxheight(root.left)
        rightheight=self.maxheight(root.right)
        print(leftheight,rightheight)
        return 1+(max(leftheight,rightheight))
