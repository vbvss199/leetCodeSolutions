class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using xor 
        # xor=nums[0]
        # n=len(nums)
        # for i in range(1,n):
        #     xor=xor^nums[i]
        # for k in range(1,n+1):
        #     xor=xor^k
        # return xor

        # using hashmap 
        freq_map={}
        n=len(nums)
        for num in nums:
            freq_map[num]=freq_map.get(num,0)+1
        for i in range(n+1):
            if(freq_map.get(i,0)==0):
                return i
        retur -1