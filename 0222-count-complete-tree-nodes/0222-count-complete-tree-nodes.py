# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeftHeight(self,root:Optional[TreeNode])->int:
        height=0
        while(root):
            height=height+1
            root=root.left
        return height
    
    def findRightHeight(self,root:Optional[TreeNode])->int:
        height=0
        while(root):
            height=height+1
            root=root.right
        return height

    def countNodes(self, root: Optional[TreeNode]) -> int:
        # traverse in any order then increment the node values lets go with the pre order
        # self.nodeCount=0
        # def dfs(node):
        #     if node is None:
        #         return
        #     else:
        #         self.nodeCount=self.nodeCount+1
        #         dfs(node.left)
        #         dfs(node.right)
        # dfs(root)
        # return self.nodeCount
        

        # lets try the optimised one 
        if root is None:
            return 0
        lh=self.findLeftHeight(root)
        rh=self.findRightHeight(root)
        # case of complete binary tree
        if(lh==rh):
            return 2**lh-1

        # if it is not a complete binary tree
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
