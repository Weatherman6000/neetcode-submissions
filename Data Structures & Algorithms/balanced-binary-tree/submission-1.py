# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True 
        else: 
            if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
                return False
            return self.isBalanced(root.left) and self.isBalanced(root.right)
