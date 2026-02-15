# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMax(self,root:Optional[TreeNode])->int:
        if root is None:
            return 0
        # dont ever considet the negayive sum path so reset to zero by finding the 
        leftSum=max(0,self.findMax(root.left))
        rightSum=max(0,self.findMax(root.right))
        # for any node to be the largest we need to sum the right and left along the node val first we will find the left height is larger depth or right one then we take the one which is max whether left or right then add the node.val and max(lh,rh)
        self.maxValue=max(self.maxValue,leftSum+rightSum+root.val)
        return max(leftSum,rightSum)+root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxValue=float('-inf')
        self.findMax(root)
        return self.maxValue
        