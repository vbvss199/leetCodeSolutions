class Solution:
    def jump(self, nums: List[int]) -> int:
        # every index has all the possible ways , so consider the minimum of all of those approaches !
        # solved using the recursive tree approach for each index explore all the possible paths and take the minimmum at each step i guess 
        # starting with the 0th index and the number of jumps will be zero inittially which is f(0,0) at f(0,0) we can take at max of nums[index] jumps 
        memo={}
        def f(index):
            # which stores the index and the minimum jumps it required from that index ! 
            # base case when we reach to the end then return ! 
            if(index >=len(nums)-1):
                return 0
            # check if the index is already computed then return it 
            if index in memo:
                return memo[index]
            # and the recursive case 
            mini=float("inf")
            for i in range(1,nums[index]+1): #for each number in nums[index] we start from 1 to the max steps !
                mini = min(mini, 1 + f(index + i))
            memo[index]=mini
            return mini
        return f(0)