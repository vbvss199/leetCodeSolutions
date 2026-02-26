# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # create hashMap using Inorder coz the root in the inroder helps us to seggregate the left and right sub trees ! 
        inMap={}
        for i in range(len(inorder)):
            inMap[inorder[i]]=i
        # after creating this calla function that calls recursively evrytime with a new in order and pre order 
        # the params we consider are preOrder,preStart,preEnd,inorder,inStart,inEnd,inMap
        return self.buildTreeWithParams(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,inMap)
    # the recursive function !
    def buildTreeWithParams(self,preorder:List[int],preStart:int,preEnd,inorder:List[int],inStart:int,inEnd:int,inMap:dict[int, int])->Optional[TreeNode]:
        # as always write the base conditions to avoid the index out of range
        if (preStart>preEnd) or (inStart>inEnd):
            return None
        # lets start this fucking shit!!!
        # find the root and start building tree!
        # dont use the sqaure braces use braces to create 
        root=TreeNode(preorder[preStart])
        inRoot=inMap[root.val]
        # find the numbers left 
        numsLeft=inRoot-inStart
        # now call the left and right recursively using the same fucntion
        # for inorder we consider the inorder to be passed is on the left array 
        # for the left the left sub tree is to the left of the inorder list !
        root.left=self.buildTreeWithParams(preorder,preStart+1,preStart+numsLeft,inorder,inStart,inRoot-1,inMap)
        # for right the right of the root from the inordder will be the right subtree
        root.right=self.buildTreeWithParams(preorder,preStart+numsLeft+1,preEnd,inorder,inRoot+1,inEnd,inMap)
        return root 