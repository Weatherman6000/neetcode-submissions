# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  

    def getTreeList(self, root):
         if not root: return []
         else: return [root] + self.getTreeList(root.left) + self.getTreeList(root.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tList = self.getTreeList(root)
        for tree in tList:
            if self.isSubtreeHelper(tree, subRoot): return True
        return False

    def isSubtreeHelper(self, root, subRoot):
        if root == None and subRoot == None: return True 
        if (root != None and subRoot == None) or (subRoot != None and root == None) or root.val != subRoot.val:
            return False
        else: return self.isSubtreeHelper(root.left, subRoot.left) and self.isSubtreeHelper(root.right, subRoot.right)