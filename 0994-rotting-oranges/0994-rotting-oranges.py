from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # if its impossible in the senseany one of the orange remains return -1
        # there may be multiple rotten oranges that can make the adjacent one spoil simulataneously 
        # visiitng the adj nodes at the same level concept ?
        # need to move at a constant space using bfs dfs explores depth each second which will take n steps , here the constraint is to take the minimum time to travel
        n=len(grid) #rows
        m=len(grid[0]) #columns 
        visited=[[-1 for _ in range(m)] for _ in range(n)]
        # directions array for th4e neighbours
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        # traverse through the bfs !!!

        # queue ds storing the pair and the time deque([(1, 2, 0)]) unpacking queue.popleft() which unpacks the row col and the time 
        queue=deque([])
        for i in range(n):
            for j in range(m):
                # get all the rotten oranges
                if(grid[i][j]==2):
                    queue.append((i,j,0))
                    # and mark the visited grid as well
                    visited[i][j]=2
                else:
                    visited[i][j]=0
        
        # initial time is 0 
        time=0
        while(queue):
            row,col,t=queue.popleft()
            time=max(t,time)
            # once we got this visit the neighbouring guys 
            for del_row,del_col in directions:
                n_row=row+del_row
                n_col=col+del_col
                if(n_row>=0 and n_row<n and n_col>=0 and n_col<m and visited[n_row][n_col]!=2 and grid[n_row][n_col]==1):
                    queue.append((n_row,n_col,time+1))
                    visited[n_row][n_col]=2
                    
        # check all of the visited r nt equl to rotten and any one of the element in the grid is 1
        for l in range(n):
            for k in range(m):
                if(visited[l][k]!=2 and grid[l][k]==1):
                    return -1
        return time
