class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # dont allocate extra space ? change the array itself !!!!
        # just return the k elements not the length !!!
        # same as two pointer leave the first element and start i and j from. 1, use the count variable if it is >2
        # start count =1 as we start from 1 
        j=1
        count=1
        n=len(nums)

        # j is the index where we gonna overide the things 
        # and i is the one where we scan the array !

        for i in range(1,n):
            # comapre the i to i -1 occurance and if there is a match then increment the cout
            if(nums[i]==nums[i-1]):
                count=count+1
            else:
                count=1
            
            if count <=2:
                nums[j]=nums[i]
                j+=1
            
            
            # and if count<=2 then we override the elemtn j 
        return j
