class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        lengths = [len(str(n)) for n in nums]
        for i in range(len(lengths)):
            if(lengths[i]%2==0):
                count=count+1
        return count