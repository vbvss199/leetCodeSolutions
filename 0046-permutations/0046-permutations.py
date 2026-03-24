# permutations of a string using bit manipulation or using recursion 
# the total number of permutations will be n ! 
class Solution:
    def generatePermutations(self,nums:List[int],ds:List[int],results:List[List[int]],hashSet)->List[List[int]]:
        #base condition will be when the index will reach the len(nums) then append it to the results and return 
        if(len(ds)==len(nums)):
            results.append(ds.copy())
            return
        for i in range(0,len(nums)):
            if nums[i] not in hashSet:
                hashSet.add(nums[i])
                # then do the logic of calling recursively 
                ds.append(nums[i])
                self.generatePermutations(nums,ds,results,hashSet)
                ds.pop()
                hashSet.remove(nums[i])
        return results
    def permute(self, nums: List[int]) -> List[List[int]]:
        hashSet=set()
        return self.generatePermutations(nums,[],[],hashSet)