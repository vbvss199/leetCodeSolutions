class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # lets go directly with binary search approach
        # k is the target
        # brute force 
        for i in range(len(arr)):
            if(arr[i]<=k):
                k=k+1
            else:
                break
        return k