class Solution:
    def findCombinationSum(self, index, arr, target, answers, ds):
        if index == len(arr):
            if target == 0:
                answers.append(ds.copy())
            return
        if arr[index] <= target:
            ds.append(arr[index])
            self.findCombinationSum(index, arr,target - arr[index], answers, ds)
            # backtracking
            ds.pop()
        self.findCombinationSum(index + 1,arr, target, answers, ds)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = []
        self.findCombinationSum(0, candidates, target, answers, [])
        return answers
