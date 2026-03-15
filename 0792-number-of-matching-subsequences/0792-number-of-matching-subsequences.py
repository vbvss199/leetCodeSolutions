class Solution:
    # def generateSubSequences(self,index,subSequence):
    #     if(index==self.n):
    #         self.subSequenceList.append("".join(subSequence))
    #         return
    #     subSequence.append(self.sList[index])
    #     self.generateSubSequences(index + 1, subSequence)
    #     # kind of back track
    #     subSequence.pop()
    #     self.generateSubSequences(index + 1, subSequence)

    # 2nd method isSubSequence using two pointers
    def isSubSequence(self,s:str,word:str)-> bool:
        i=0 #for str
        j=0 #for word
        while i <len(s) and j < len(word):
            if(s[i]==word[j]):
                j=j+1
            i=i+1
        return j==len(word)
        

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # self.subSequenceList=[]
        # self.sList=[c for c in s]
        # self.n=len(self.sList)
        # self.generateSubSequences(0,[])
        # count=0

        # # now we have two list subSequenceList and given words compare them and return the count
        # for w in words:
        #     if w in self.subSequenceList:
        #         count=count+1
        # return count

        # 2nd approach using two pointer
        memo={}
        count=0
        for word in words:
            if word not in memo:
                memo[word]=self.isSubSequence(s,word)
            if memo[word]:
                count=count+1
        return count


# lets solve this by recursion
        # strivers solution was taken the numbers into consideration while here it is characters
        # recursion using base case and the recursive condition 
        # the code goes like
        # fun(index,subsequenceslist):
        # if index>=n:
        # print or store in list of lists 
        # return
        # subsequenceslist.append(arr[i])
        # fun(index+1,subsequenceslist). -> condition of take 
        # pop the element
        # subsequenceslist.remove[arr[i]]
        # fun(index+1,subsequenceslist) > condition of not take 
        # if we have an array [3,1,2] index=0 pass this to fun(0,subsequenceslist)
        # as the first case is not executed add the first element to the arrray ok we took the index+1 and pass on the [3] to the function again the base case is not executed
        # so add [3].add([1]) now index+1 which is 2 fun(2,[3,1]) this function call will go now 
        # next again function call if statemnet is not executed so add it array becomes [3,1,2]
        # the next call is [3,1,2] with index 3 now the if condition is executed and returned 
        # so returning to the previous case where index is 2 and now we have a chance of not picking up 
        # so in the next iteration we pop the element and call the function with the array again
