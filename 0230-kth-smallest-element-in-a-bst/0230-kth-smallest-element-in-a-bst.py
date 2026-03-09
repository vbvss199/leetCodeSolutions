# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do in order traversal as it is a bst, in inorder we go left and print root and then right so by defualt the in order traversal 
        # will be the sorted array 
        stack=[]
        # as we already know the arry will be sorted increment the count and retuen the integer when it is equal to k 
        # or just save the node values in the result array and return the k the element 
        count=0
        current=root
        while(stack or current):
            while(current is not None):
                # traverse to the extreme left and push the nodes to stack!
                stack.append(current)
                current=current.left
            # when it is none incrmenet the counter coz we r at the root node
            node=stack.pop()
            count=count+1
            if(count==k):
                return node.val
            # not the current.right it must be node.right fucking blind im
            current=node.right
