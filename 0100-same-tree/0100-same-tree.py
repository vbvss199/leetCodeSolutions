# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # how to approach this ???t
        # if p is None and q is None:
        #     return True
        # if p is None or q is None:
        #     return False
        # if(p.val!=q.val):
        #     return False
        # return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        # # mottam recursion tappa em ledhu !!!

        # this can be done using the pre order and in order traversal as well do the pre order and inorder traversak and compare both the arrays 
        # lets do this approach Approach2
        l1=self.preOrder(p)
        l2=self.preOrder(q)
        if l1==l2:
            return True
        else:
            return False 
    # to calculate the in order of tree 
    def preOrder(self,root:Optional[TreeNode])->list:
        l=[]
        if root is None :
            l.append(None)
            return l
        else:
            l.append(root.val)
            l=l+self.preOrder(root.left)
            l=l+self.preOrder(root.right)
        return l


# for any pre or in or post to work we need to cosidet the None as well so if it is none 