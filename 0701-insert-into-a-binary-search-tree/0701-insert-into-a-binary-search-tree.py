# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLead(self,node:Optional[TreeNode])-> bool:
        if(node.left is None and node.right is None):
            return True
        return False
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # tree needs to be balanced after the insertion !
        # so based on the given integer go left it it is small else go right then stop at the leaf node attach to it based on the value to left or right 
        if root is None:
            return TreeNode(val)
        curr=root
        while True:
            if(val<=curr.val):
                # move left 
                if curr.left is None:
                    newNode=TreeNode(val)
                    curr.left=newNode
                    break
                curr=curr.left
            else:
                if curr.right is None:
                    newNode=TreeNode(val)
                    curr.right=newNode
                    break
                curr=curr.right
        return root
            
