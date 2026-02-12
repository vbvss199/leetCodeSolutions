# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        # def inorder(node):
        #     if node is None:
        #         return
        #     else:
        #         inorder(node.left)
        #         result.append(node.val)
        #         inorder(node.right)
        # inorder(root)
        # return result
        if root is None:
            return []
        else:
            stack=[]
            curr=root
            while(curr or stack):
                while curr:
                    stack.append(curr)
                    curr=curr.left
                # process the current node
                curr=stack.pop()
                result.append(curr.val)
                curr=curr.right
            return result











#       1
#      / \
#     2   3
#    /
#   4

# Inorder = Left → Root → Right
# Let’s trace:
# Start at 1
# Go left → 2
# Go left → 4
# Go left → None (stop)
# Append 4
# Go right of 4 → None
# Back to 2
# Append 2
# Go right of 2 → None
# Back to 1
# Append 1
# Go right → 3
# Append 3

# Go left recursively
# Append current node value
# Go right recursively