class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # same as the subarray with the xor =0 instead of k
        #better approach ---> passed 99/114 test cases lets go with the optimal approach
        # count=0
        # for i in range(len(nums)):
        #     xor=0
        #     for j in range(i,len(nums)):
        #         xor=xor^nums[j]
        #         if(xor==0):
        #             count=count+1
        # return count

        # optimal approach
        count=0
        xor=0
        xorMap={0:1}
        for i in range(len(nums)):
            xor=xor^nums[i]
            # some bullshit logic like xor^k or something 
            if xor in xorMap:
                count += xorMap[xor]
            xorMap[xor]=xorMap.get(xor,0)+1
        return count