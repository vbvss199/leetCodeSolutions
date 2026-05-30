class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # sequentially adjacent meaning horizantal or vertically neighbouring cells , and same letter cell may not be used more than once 
        # may be like in the given grid we go the starting word and start exploring all the paths from the word ?
        # we use back tracking if we dont find it !!!!!! 
        m=len(board)
        n=len(board[0])
        w=len(word)

        if(m==1 and n==1):
            return board[0][0]==word
        def backtrack(pos,index):
            i,j=pos

            # if we reach the end then we return true 
            if(index==w):
                return True
            
            # if the path we r looking is not equal to the board 
            if(board[i][j]!=word[index]):
                return False
            
            # some how if it is not false taht means theres a possibility now check all the four sides 
            # before that mark the board path as # 
            # save the char at the place so if it is not happening we replace the chat 
            char=board[i][j]
            board[i][j]="#"

            # now we do dfs 
            for i_off,j_off in [(0,1),(1,0),(0,-1),(-1,0)]:
                # based on these values our r and c will be 
                r,c=i+i_off,j+j_off
                if 0<=r<m and 0<=c<n:
                    if(backtrack((r,c),index+1)):
                        return True
            # if we dint find any path then keep the char back 
            board[i][j]=char
            return False 

        # for each position in the matrix we need to do backtracking 
        for i in range(m):
            for j in range(n):
                if(backtrack((i,j),0)):
                    return True
        
        # if we r done with every single position and we dint find anything then we return false 
        return False 