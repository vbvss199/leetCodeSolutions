# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self,root:Optional[TreeNode])-> int:
        if root is None:
            return 0
        else:
            leftHeight=self.maxDepth(root.left)
            rightHeight=self.maxDepth(root.right)
            if(leftHeight==-1 or rightHeight==-1):
                return -1

            # 1check this condition first the above one im wiriting is with reference to the abs(l-r) as at any moment it is >1 we returned -1 so it is travered back so we check again if leftHeight or rightHeight is equal to -1 then we return -1
            if(abs(leftHeight-rightHeight))>1:
                return -1
            return 1 + max(leftHeight,rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        k=self.maxDepth(root)
        if(k==-1):
            return False
        else:
            return True

        