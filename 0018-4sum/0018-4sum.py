class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # uniqueList=[]
        uniqueSet=set()
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                freqMap={}
                for k in range(j+1,len(nums)):
                    sum=nums[i]+nums[j]+nums[k]
                    kterm=target-sum
                    if kterm in freqMap:
                        quad=tuple(sorted([nums[i],nums[j],nums[k],kterm]))
                        uniqueSet.add(quad)
                    freqMap[nums[k]]=freqMap.get(nums[ k ], 0) + 1
        return list(uniqueSet)