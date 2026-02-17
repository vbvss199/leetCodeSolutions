# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def comparision(self,left: Optional[TreeNode],right: Optional[TreeNode])->bool:
        if(left is None and right is None):
            return True
        if(left is None or right is None):
            return False
        if(left.val!=right.val):
            return False
        return self.comparision(left.left,right.right) and self.comparision(left.right,right.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left=root.left
        right=root.right
        return self.comparision(left,right)