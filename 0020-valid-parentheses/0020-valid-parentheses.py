class Solution:
    def isValid(self, s: str) -> bool:
        # lets see if can be solved using the two pointer
        # s=''.join(c.lower() for c in s if c.isalnum() )
        # left=0
        # right=len(s)-1
        # while(left<right):
        #     # check for the condition to break like not equal the moment they are not equal return false
        #     if(s[left]!=s[right]):
        #         return False
        #     left=left+1
        #     right=right-1
        # return True
        stack=[]
        mapping={
            ')': '(', ']': '[', '}': '{'
        }
        for ch in s:
            if(ch in mapping):
                # check if it is in the top of the stack 
                if not stack or stack[-1]!=mapping[ch]:
                    return False
                stack.pop()
            else:
                #closing condition push to the stack
                stack.append(ch)
        return len(stack) == 0


        # open bracket push to the stack 
        # close bracket then pop match and remove it ?
        # s = "([{}])"
        # 1. opening( -> push 2.opening[ ->push 3.opening{ -> push 4th closing which is in the mapping so check the top of of the stack 
