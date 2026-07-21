from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def getTreeList(self, root: Optional[TreeNode]) -> list:
        if root == None:
            return []
        else:
            return [root] + self.getTreeList(root.left) + self.getTreeList(root.right)    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0
        treeList = self.getTreeList(root)
        for tree in treeList:
            diameter = self.maxDepth(tree.left) + self.maxDepth(tree.right)
            if diameter > longest:
                longest = diameter
        return longest

        
       