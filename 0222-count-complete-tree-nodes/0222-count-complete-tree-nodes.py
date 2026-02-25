# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # traverse in any order then increment the node values lets go with the pre order
        self.nodeCount=0
        def dfs(node):
            if node is None:
                return
            else:
                self.nodeCount=self.nodeCount+1
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.nodeCount
        