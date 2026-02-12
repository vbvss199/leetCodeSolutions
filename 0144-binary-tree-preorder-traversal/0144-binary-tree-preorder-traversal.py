# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # l=[]
        # def dfs(node):
        #     if node is None:
        #         return
        #     else:
        #         l.append(node.val)
        #         dfs(node.left)
        #         dfs(node.right)
        # dfs(root)
        # return l

        # approach2 using stack and iteration 
        if root is None:
            return []
        else:
            results=[]
            stack=[]
            stack.append(root)
            while(stack):
                node=stack.pop()
                results.append(node.val)
                # as pre order is first left then right ,but stack follows the reverse order so first right then left
                if(node.right):
                    stack.append(node.right) 
                if(node.left):
                    stack.append(node.left)
        return results
        