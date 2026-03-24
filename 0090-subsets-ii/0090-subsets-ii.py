# for this watch the combinations sum 2 
class Solution:
    def subsetsGenerator(self,nums:List[int],index,ds,results)->List[List[int]]:
        results.append(ds.copy())
        # now continue with the pick and not pick logic 
        for i in range(index,len(nums)):
            if(i>index and nums[i]==nums[i-1]):
                continue
            ds.append(nums[i])
            self.subsetsGenerator(nums,i+1,ds,results)
            ds.pop()
        return results 
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.subsetsGenerator(nums,0,[],[])