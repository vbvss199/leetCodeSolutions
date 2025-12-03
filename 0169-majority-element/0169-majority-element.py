class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # freqMap={}
        # n=len(nums)
        # for i in range(len(nums)):
        #     freqMap[nums[i]]=freqMap.get(nums[i],0)+1
        # max_key = max(freqMap, key=freqMap.get)
        # return max_key

        # let's try the moore's voting algorithm
        element =nums[0]
        count=0
        for i in range(len(nums)):
            if(nums[i]==element):
                count=count+1
            else:
                count=count-1
                if(count==0):
                    element=nums[i+1]
                else:
                    continue
        return element 