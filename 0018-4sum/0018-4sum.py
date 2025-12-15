class Solution:
    # O(n^3 ) time complexity using hashing and
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     uniqueSet=set()
    #     for i in range(0,len(nums)):
    #         for j in range(i+1,len(nums)):
    #             freqMap={}
    #             for k in range(j+1,len(nums)):
    #                 # carefull dont accumulate
    #                 sum=nums[i]+nums[j]+nums[k]
    #                 kterm=target-sum
    #                 if kterm in freqMap:
    #                     quad=tuple(sorted([nums[i],nums[j],nums[k],kterm]))
    #                     uniqueSet.add(quad)
    #                 freqMap[nums[k]]=freqMap.get(nums[ k ], 0) + 1
    #     return list(uniqueSet)

    # lets get to the optimal approach using the pointer 
        nums.sort()
        n=len(nums)
        uniqueList=[]
        for i in range(n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            # as j is the second element so we took i+1
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k, l = j + 1, n - 1
                while(k<l):
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if(sum==target):
                        quad=[nums[i],nums[j],nums[k],nums[l]]
                        uniqueList.append(quad)
                        k=k+1
                        l=l-1
                        while(k<l and nums[k] ==nums[k-1]):
                            k=k+1
                        while(k<l and nums[l]==nums[l+1]):
                            l=l-1
                    elif (sum < target):
                        k=k+1
                    else:
                        l=l-1
        return uniqueList
