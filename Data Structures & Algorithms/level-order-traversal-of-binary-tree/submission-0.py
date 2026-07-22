# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        que = deque()
        que.append(root)
        level = []
        while not len(que) == 0:
            currLength = len(que)
            sublevel = []
            for i in range(currLength):
                tree = que.popleft()
                sublevel.append(tree.val)
                if tree.left != None:
                    que.append(tree.left)
                if tree.right != None:
                    que.append(tree.right)
            level.append(sublevel)
        return level

            
