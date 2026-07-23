class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # maintains the order in the string we can skip the chars but order is important 
        # in order to print all the sub sequences we fo for powerset or recursion , 
        # ** empty string is also a sub sequence PERIOD !!!!
        # for a given n there will be 2^n subsequences !! starting from the every charcter of the given string 
        # option 1: generate all the sub sequences for both the strings and find the one which is the longest and common of the both 
        # brute force is exponential using power set or recursion !!!!!
        # cosider the recurrance relation using both the indices and then propagate 
        # the conditions are like match and non match scenarios !!!
        # for the match scenari increment both the indices by 1 and add one in sub sequent matches 
        # for the non matches scenarios as follows 
        # non match so add 0 0+max(f(index1-1,index2),f(index1,index2-1))


        # consider the recursive approach 

        def traverse(index1,index2,dp):
            # check if it is going <0 
            if(index1<0 or index2<0):
                return 0
            
            # check if it is there then return the value from the dp
            if (index1,index2) in dp:
                # then return the value 
                return dp[(index1,index2)]

            # check if both of the chars at the indices are equal 
            if(text1[index1]==text2[index2]):
                # call the function recursively with the new index 
                dp[(index1,index2)]= 1+traverse(index1-1,index2-1,dp)

            # here comes the one with no match of the strings!!
            else:
                dp[(index1,index2)]= max(
                                    traverse(index1-1,index2,dp),
                                    traverse(index1,index2-1,dp)
                                    )
            return dp[(index1,index2)]


        # call the function with the last indices !!
        # optimisation step using map, so storing looks like dp[(index1, index2)]
        dp = {}
        return traverse(len(text1)-1,len(text2)-1,dp)


# when will the base caee will come ?think about the negative case in the max() when it goes by -1 everytime and if it reaches <0 then thats done 