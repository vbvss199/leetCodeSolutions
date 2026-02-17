# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderTraversal(self,root:Optional[TreeNode])-> Map[List[int]]:
        queue=deque()
        queue.append((root,0,0))
        while(queue):
            size=len(queue)
            for i in range(size):
                node,vertical,horizontal=queue.popleft()
                if vertical not in self.someXMap:
                    self.someXMap[vertical]=[]
                self.someXMap[vertical].append((horizontal,node.val))
                if node.left:
                    queue.append((node.left,vertical-1,horizontal+1))
                if node.right:
                    queue.append((node.right,vertical+1,horizontal+1))
        return self.someXMap


    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # the idea was to do any traversal (in or pre or post) i will be going with the level order 
        # then saving the coordinates of the each level along with the nodes i.e node.val and vertical and horizontal 
        if root is None:
            return []
        # this must be a special data structure to store the data values and the vertical and horizantal cordinates i guess 
        self.someXMap={}
        finalMap=self.levelOrderTraversal(root)
        # after the in order traversal we got the map which looks like
        # {
        #     -1:[(0,3),(1,2)]
        #     0:...
        #     1:....
        # }
        # now traverse across the vertical levels and print the data
        levels=[]
        for verticalLine in sorted(finalMap.keys()):
            column=sorted(finalMap[verticalLine])
            values = []
            for item in column:
                values.append(item[1])
            levels.append(values)
        return levels
        