class Solution:
    def simplifyPath(self, path: str) -> str:
        # multiple slashes treated as single slash 
        # if it is not a single or double period then we treat them as directory or file names 
        # path must start with the single slash 
        # directories with in the path r separated by one slash 
        # path should nt end with a slash 
        # .. dots go back two directories or paths or pop one dir we can use stack 
        # if we encounter .. then call the pop function 
        stack=[]
        # curr is the current file path that is before the / 
        
        # split will be based on the / so empty string will come !!!
        for part in path.split("/"):
            if part=="" or part==".":
                continue 
            elif(part==".."):
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        # after this we get the stack with empty spaces and the directoriy names so join them accordingly 
        # if "/home/" then split divides in this way ! ["","home",""] as there are two / 
        return "/" + "/".join(stack)
        
        # Index:  0123456789
        # Path : / h o m e / / f o o /
        # stack=[]
        # i=0
        # n=len(path)

        # while i<n:
        #     # skip the / 
        #     while i <n and path[i]=="/":
        #         i=i+1
        #     # so if it is not the case then we need to start counting the chars of the string 
        #     name=""
        #     # second loop 
        #     while i <n and path[i]!="/":
        #         name=name+path[i]
        #         i=i+1
            
        #     # if name is . or "" then move forward 
        #     if name=="" or name==".":
        #         continue 
            
        #     # now look for the .. 
        #     elif (name==".."):
        #         if stack:
        #             stack.pop()
            
        #     else:
        #         stack.append(name)

        # return "/" + "/".join(stack)
            