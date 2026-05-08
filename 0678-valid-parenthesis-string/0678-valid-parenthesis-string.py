class Solution:
    def checkValidString(self, s: str) -> bool:
        # replace the astrick with anything such that it becomes the valid parenthesis !  
        # check for the parenthesis and count one if it is opening and remove one if it is closing and check the count if it is zero cvalid at any moment if the count is -1 then break and return false ! 
        # using recursion call repeatdly checkValidString using different scenarios for the * try find out all the combinations !
        
        count=0 #same logic here as well see in any case we can fit the astrick and satisfy 
        
        # #approach 1 
        # def check(s,count,index):
        #     if(count<0):
        #         return False
        #     if(index==len(s)):
        #         return count==0
        #     if s[index] == "(":
        #         return check(s,count+1,index+1)
        #     elif s[index]== ")":
        #         return check(s,count-1,index+1)
        #     else:
        #         # call recursively the funciton with the possible braces which are (  or )
        #         # case 1 with open brace then add the count 
        #         return (check(s,count+1,index+1) or check(s,count-1,index+1) or check(s,count,index+1))
                # casee 2 closed parenthesis then remove the count 
                # case 3 empty just remove the astrick and send it to check 
        # return check(s,count,0)
        # the time complexity as three branches formed so 3^N in worst case if all of them are * and if one * then 3 so on 
        # using dynamic programming what we do is as index ranges from 0 to n-1 and count from 0 to n dp[n][n] and memoise it 
        # and using this the time complexity will be O(n2) and space iwll be O(n) 

        # approach 2 
        # we still stick with the brute force but with the better optimisation now !
        # at astrick we can have 3 combinations so try to fill the max and min variables using this count logic
        # so for the three possiblities the range may go from -1 to 1 so we carry the max and min instead ofthe count 
        # if it is a opening the range will be min=1 max=1 if it is a closing then min =0 max=0 and there comes a astrick if it is a * we can do +1 or 0 or -1 , and if the current is 0 and a closing brace then -1 so we dont considet that instead we consider the other cases and re assign the max and min variables using that , so min will be [0,1] and max willl be [0,1] so instead we store min =0 max=1
        min=0
        max=0
        for ch in s:
            if ch=="(":
                min=min+1
                max=max+1
            elif ch==")":
                min=min-1
                max=max-1
            else:
                # consition where it is * 
                # three possible cases where (  or ) or empty where we wont add anything 
                # we need to some math and assignnthe range to min and max such that it shouldnt go beyond -1 
                # so for the min and max check out the possibilities and keep the one which are possible >0 
                min=min-1
                max=max+1
            if(min<0):
                min=0
            if(max<0):
                return False
        return min==0