class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # province is a group of cities so if two are connected then two separate provinces and if three connected then a single province 
        # try to create a adjacency list from the matrix 
        adj = [[] for _ in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                # check if there is a node and make sure it is not a self node 
                if(isConnected[i][j]==1 and i!=j):
                    adj[i].append(j)
                    adj[j].append(i)

        # once we r donw with this then our adjacency list is there 
        visited=set()
        
        def dfs(node):
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        # provices count
        count=0
        for i in range(len(adj)):
            if i not in visited:
                dfs(i)
                count=count+1
            
        return count 