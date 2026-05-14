class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # allowed only in four directions so  if we r standing at the origin 
        # directions=[(-1,0),(1,0),(0,-1),(0,1)], but upon the directions we only mark the one which has the same color 
        # similar to the number of islands here we use DFS instead of BFS to solve this 
        def dfs(output_mat,sr,sc,color,directions,initial_color):
            # so when we come here we need to make the color of the row,col to the new color 
            # instead of changing the matrix consider the new matrix and change it 
            output_mat[sr][sc]=color
            # after coloring them now look for the ones which are adjacent only in horizantal and vertical wise 
            for del_row,del_col in directions:
                n_r=sr+del_row
                n_c=sc+del_col
                # check if this is a valid guy
                if(n_r>=0 and n_r<len(image) and n_c>=0 and n_c<len(image[0]) and image[n_r][n_c]==initial_color and image[n_r][n_c]!=color):
                    dfs(output_mat,n_r,n_c,color,directions,initial_color)

        output_mat = image.copy()
        # send the directions to the dfs to explore its neighbours !
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        # call the function with the params
        # initial_color
        initial_color=image[sr][sc]
        dfs(output_mat,sr,sc,color,directions,initial_color)
        return output_mat