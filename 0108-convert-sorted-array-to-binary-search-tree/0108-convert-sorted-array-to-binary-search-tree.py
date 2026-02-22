# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # balanced tree is one which is having the left and right heights are same 
        def build(start,end):
            if start > end:
                return None
            mid=(start+end)//2
            root=TreeNode(nums[mid])
            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)

            return root
        return build(0,len(nums)-1)
        