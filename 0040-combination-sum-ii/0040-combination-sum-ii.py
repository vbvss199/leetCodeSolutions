class Solution:
    def findCombinations2(self,idx,candidates:List[int],target:int,ds:List[int],results:List[List[int]]) -> List[List[int]]:
        if(target==0):
            results.append(ds.copy())
            return
        for i in range(idx,len(candidates)):
            if(i>idx and candidates[i]==candidates[i-1]):
                continue
            if(candidates[i]>target):
                break
            ds.append(candidates[i])
            self.findCombinations2(i+1,candidates,target-candidates[i],ds,results)
            ds.pop()
        return results
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.findCombinations2(0,candidates,target,[],[])