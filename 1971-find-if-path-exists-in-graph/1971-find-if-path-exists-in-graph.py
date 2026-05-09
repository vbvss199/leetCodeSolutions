class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=[[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # created a visited set such it marks the given element as true or false
        visited=set()

        # and do a bfs or dfs until the destimation is found!
        def dfs(node):
            if node==destination:
                return True
            visited.add(node)

            # lets see how the logic builds here 
            for neighbour in graph[node]: #if node 0 then [1,2] for neighbours in [1,2], so it goes two iterations now ! 
            # first iteration it will be 1 and second will be 2 
            # if the neighbour is not visited then go recursively
                if neighbour not in visited:
                    if(dfs(neighbour)):
                        return True
            return False
        
        # call dfs
        return dfs(source)
