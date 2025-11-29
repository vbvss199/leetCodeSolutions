class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mpp={}
        for num in nums:
            mpp[num]=mpp.get(num,0)+1
        sorted_list_tuples=sorted(mpp.items(),key=lambda x:x[1],reverse=True)
        #this one returns list with tuples
        #need to find the number of elements with the max frequency ,and if there are unique elements we need to return the lenght i guess simply
        #case 1 if there is only one max _frequency return that
        #case 2 if there is no such frequency then return length
        #case 3 if there are more than 2 return combined 
        max_freq=max(mpp.values())
        total=0
        for freq in mpp.values():
            if(freq==max_freq):
                total=total+freq
        return total


        