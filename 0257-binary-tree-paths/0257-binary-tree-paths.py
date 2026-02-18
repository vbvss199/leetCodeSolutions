# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node:Optional[TreeNode],nodestrings:str):
        # traverse left and right recursively and store the values to right and left 
        if(node.left is None and node.right is None):
            self.treePaths.append(nodestrings+str(node.val))
            return
        nodestrings=nodestrings+str(node.val)+"->"    
        if(node.left):
            self.dfs(node.left,nodestrings)
        if(node.right):
            self.dfs(node.right,nodestrings)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.treePaths=[]
        if root is None:
            return []
        # traverse left and store the paths in the queue may be then traverse the right ans save them in the queue 
        self.dfs(root,"")
        return self.treePaths
        