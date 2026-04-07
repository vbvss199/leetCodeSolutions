class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxLength=0
        left=0
        count=defaultdict(int)
        for right in range(0,len(fruits)):
            count[fruits[right]]+=1
            while(len(count)>2):
                count[fruits[left]]-=1
                if(count[fruits[left]]==0):
                    del count[fruits[left]]
                left=left+1
            if(len(count)<=2):
                maxLength=max(right-left+1,maxLength)
        return maxLength