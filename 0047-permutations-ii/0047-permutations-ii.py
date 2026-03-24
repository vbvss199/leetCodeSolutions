class Solution:
    def generatePermutations(self,nums:List[int],ds:List[int],results:List[List[int]],used)->List[List[int]]:
        #base condition will be when the index will reach the len(nums) then append it to the results and return 
        if(len(ds)==len(nums)):
            results.append(ds.copy())
            return        
        for i in range(0,len(nums)):
            if used[i]:
                continue
            # skip duplicates
            # Always use duplicates in order”
            # “Skip duplicate if previous identical element is NOT used”
            if (i >0 and nums[i]==nums[i-1] and not used[i-1]):
                continue
            used[i]=True
            # then do the logic of calling recursively 
            ds.append(nums[i])
            self.generatePermutations(nums,ds,results,used)
            ds.pop()
            used[i]=False
        return results
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # as hashmap works with the values so we go with the used array
        used=[False]*len(nums)
        return self.generatePermutations(nums,[],[],used)
        