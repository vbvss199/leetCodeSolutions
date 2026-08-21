class Solution:
    def countAndSay(self, n: int) -> str:
        #lets start with 1 
        res="1"
        for i in range(1,n):
            newData=""
            current=res[0]
            count=1
            for c in res[1:]:
                if(c==current):
                    count+=1
                else:
                    newData=newData+str(count)+current
                    current=c
                    count=1
            res=newData+str(count)+current
        return res