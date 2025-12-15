class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        # simple brute force getting fucked up due to TLE error use the optimised one 
        # passed 310/315 TEST CASES 
        # uniqueSet=set()
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if(nums[i]+nums[j]+nums[k]==0):
        #                  triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                  uniqueSet.add(triplet)
        # return list(uniqueSet)


        #  Better approach TESTCASES 313/315
        #  lets go with a optimal one
        # uniqueSet=set()
        # for i in range(len(nums)):
        #     freqMap={}
        #     for j in range(i+1,len(nums)):
        #         #find the third element 
        #         k=-(nums[i]+nums[j])
        #         #find if the element if it is  in the  hashmap
        #         if k in  freqMap:
        #             #then add the triplet to set
        #             triplet=tuple(sorted([nums[i],nums[j],k]))
        #             uniqueSet.add(triplet)
        #         #everytime j moves we need to 
        #         freqMap[nums[j]]=freqMap.get(nums[ j ], 0) + 1
                
        #         #then return the list(uniqueSet)
        # return list(uniqueSet)

        # finally the optimised one using the two pointer approach 
        # take care of the duplicates 
        
        nums.sort()
        uniqueList=[]
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            j, k = i + 1, len(nums)- 1
            while j < k:
                sum=nums[i]+nums[j]+nums[k]
                if(sum==0):
                    triplet=[nums[i],nums[j],nums[k]] 
                    uniqueList.append(triplet)
                    j=j+1
                    k=k-1
                    # if the elements on the j and j-1 are same
                    while j < k and nums[j] == nums[j - 1]:
                        j=j+1
                    # if elements on k and k-1 are same 
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k=k-1
        return uniqueList

