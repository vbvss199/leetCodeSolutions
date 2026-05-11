from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # define a array 2d with the false initially which is a visited array 
        r=len(grid)
        c=len(grid[0])
        visited=[["0" for _ in range(c)] for _ in range(r)]
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(row,col):
            # pass radially using the rows 
            # initilise the queue with the [] iterable with the given node and check foe the neighbours radially
            queue=deque([(row,col)])
            # as we move forward we remove it from the queue and append if it has neighbours radially 
            # and add the particualr node to the visited 
            visited[row][col]="1"
            while(queue):
                # now do the bfs radially like horizant vertical and both in diagnoal wise 
                # get the row and column using the queue 
                row,col=queue.popleft()

                # write logic to visit radially i.e visiting the neighbour nodes 
                # neighbours in the sense which are not visited and having a value of 1 so there will be 8 possibilities aroun the , so row varies from row-1 row row+1 and col-1 col and col+1
                # so run loops i.e delta row from -1 to 1 and delta col from -1 to +1
                # for del_row in range(-1,2):
                #     for del_col in range(-1,2):
                for del_row, del_col in directions:
                        # if del_col==0 and del_row==0:
                        #     continue
                    neighbour_row=row+del_row
                    neighbour_col=col+del_col
                    if(neighbour_row >=0 and neighbour_row<r and neighbour_col>=0 and neighbour_col<c and grid[neighbour_row][neighbour_col]=="1" and visited[neighbour_row][neighbour_col]=="0"):
                        visited[neighbour_row][neighbour_col]="1"
                        queue.append((neighbour_row,neighbour_col))
                
        
        # islands var
        islands=0
        # as we r not building the adjacency list we iterate the matrix and 
        for row in range(r):
            for col in range(c):
                if(visited[row][col]=="0" and grid[row][col]=="1"):
                    islands=islands+1
                    bfs(row,col)
        return islands

