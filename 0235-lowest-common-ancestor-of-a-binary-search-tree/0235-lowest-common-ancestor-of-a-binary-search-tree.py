# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # as p is from left and q is from right so root must be in between the p and q 
        if root is None:
            return None
        current=root
        if ((p.val<current.val) and (q.val<current.val)):
            return self.lowestCommonAncestor(current.left,p,q)
        if ((p.val > current.val) and (q.val > current.val)):
            return self.lowestCommonAncestor(current.right,p,q)
        return root 
