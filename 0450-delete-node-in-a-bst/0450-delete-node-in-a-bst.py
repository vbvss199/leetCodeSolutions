# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val==key:
            return self.helper(root)
        curr=root
        while(curr is not None):
            if(curr.val>key):
                # move left
                if((curr.left) and  (curr.left.val==key)):
                    # this is the root we looking for send this root to the helper method
                    curr.left=self.helper(curr.left)
                    break
                else:
                    curr=curr.left
            else:
                # move right
                if((curr.right) and (curr.right.val==key)):
                    curr.right=self.helper(curr.right)
                    break
                else:
                    curr=curr.right
        return root
    def helper(self,root:Optional[TreeNode])->Optional[TreeNode]:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        rightChild=root.right
        lastRight=self.findLastRight(root.left)
        lastRight.right=rightChild
        return root.left
    
    def findLastRight(self,root:Optional[TreeNode])->Optional[TreeNode]:
        while(root.right):
            root=root.right
        return root

        