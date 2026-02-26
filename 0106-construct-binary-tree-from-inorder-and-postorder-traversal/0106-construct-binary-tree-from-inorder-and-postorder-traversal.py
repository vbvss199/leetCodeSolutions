# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # same as the previous one #105 problem but in post order we consider the last element to be the root of the Tree
        inMap={}
        for i in range(len(inorder)):
            inMap[inorder[i]]=i
        return self.buildTreeWithParams(postorder,0,len(postorder)-1,inorder,0,len(inorder)-1,inMap)
    
    def buildTreeWithParams(self,postOrder:List[int],postStart:int,postEnd:int,inOrder:List[int],inStart:int,inEnd:int,inMap:dict[int,int]):
        if inStart>inEnd or postStart>postEnd:
            return None
        # same shit again
        root=TreeNode(postOrder[postEnd])
        inRoot=inMap[root.val]
        # numbers left in inRoot from start to inroot
        numsLeft=inRoot-inStart

        # now call recursively using post and in params !
        root.left=self.buildTreeWithParams(postOrder,postStart,postStart+numsLeft-1,inOrder,inStart,inRoot-1,inMap)
        root.right=self.buildTreeWithParams(postOrder,postStart+numsLeft,postEnd-1,inOrder,inRoot+1,inEnd,inMap)
        return root