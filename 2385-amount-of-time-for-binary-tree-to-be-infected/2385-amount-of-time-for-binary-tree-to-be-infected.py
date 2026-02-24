# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def markParents(self,root:Optional[TreeNode]):
        queue=deque()
        queue.append(root)
        while(queue):
            current=queue.popleft()
            if current.left:
                self.parentTrack[current.left]=current
                queue.append(current.left)
            if current.right:
                self.parentTrack[current.right]=current
                queue.append(current.right)
    def findStart(self,root:Optional[TreeNode],start:int) -> TreeNode:
        if root is None:
            return None
        if root.val==start:
            return root
        left = self.findStart(root.left, start)
        if left:
            return left
        return self.findStart(root.right, start)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.parentTrack={}
        # mark the parents 
        self.markParents(root)
        # now make the second bfs and increment the distance and return it i guess 
        visited=set()
        queue=deque()
        # start is not a treenode we r given with value so find the node with the start value 
        startNode=self.findStart(root,start)

        # now we got the startNode start the bfs again and add the nodes to visited if they r not there add to queue and increment the distance for each level and return the distance 
        queue.append(startNode)
        visited.add(startNode)
        distance=0
        while(queue):
            size=len(queue)
            for i in range(size):
                current=queue.popleft()
                # now start the radial movement 
                if current.left and current.left not in visited:
                    queue.append(current.left)
                    visited.add(current.left)
                # now the right movement 
                if current.right and current.right not in visited:
                    queue.append(current.right)
                    visited.add(current.right)
                if current in self.parentTrack and self.parentTrack[current] not in visited:
                    queue.append(self.parentTrack[current])
                    visited.add(self.parentTrack[current])
            distance=distance+1
        return distance-1

        