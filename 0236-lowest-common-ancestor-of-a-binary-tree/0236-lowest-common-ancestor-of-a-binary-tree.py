# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findPath(self,root,target,path)->bool:
        if root is None:
            return False
        path.append(root)
        if(root==target):
            return True
        if(self.findPath(root.left,target,path) or self.findPath(root.right,target,path)):
            return True
        path.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1=[]
        path2=[]
        self.findPath(root,p,path1)
        self.findPath(root,q,path2)
        # next compare l1 and l2 and return the last matched node in both the lists 
        ancestorNode=0
        i=0
        while i <len(path1) and i<len(path2):
            if path1[i]==path2[i]:
                ancestorNode=path1[i]
            i=i+1
        return ancestorNode
        