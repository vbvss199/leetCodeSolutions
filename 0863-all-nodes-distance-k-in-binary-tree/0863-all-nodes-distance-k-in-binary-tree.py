# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def markParents(self,root:TreeNode) ->  Dict[TreeNode, TreeNode]:
        queue=deque()
        queue.append(root)
        while(queue):
            current=queue.popleft()
            if current.left:
                self.parentTrack[current.left]=current
                queue.append(current.left)
            if(current.right):
                self.parentTrack[current.right]=current
                queue.append(current.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # map for the parent tracking
        self.parentTrack={}
        self.markParents(root)
        # map for the visited nodes tracking
        visited=set() #we carw about only the the existance
        # now do the bfs again but here use the visited array and the distance variable using them and the queue DS stop it when the distance becomes 2 !
        # radiate equally through all the nodes in all directions 
        queue=deque()
        queue.append(target)
        visited.add(target)
        distance=0
        while(queue):
            if(distance==k):
                break
            size=len(queue)
            for i in range(size):
                current=queue.popleft()
                if(current.left and current.left not in visited):
                    queue.append(current.left)
                    # visited[current.left]=True
                    visited.add(current.left)
                if(current.right and current.right not in visited):
                    queue.append(current.right)
                    # visited[current.right]=True
                    visited.add(current.right)
                if(current in self.parentTrack and self.parentTrack[current] not in visited):
                    queue.append(self.parentTrack[current])
                    # visited[self.parentTrack[current]]=True
                    visited.add(self.parentTrack[current])
            distance=distance+1
        result=[]
        while(queue):
            node=queue.pop()
            result.append(node.val)
        return result
