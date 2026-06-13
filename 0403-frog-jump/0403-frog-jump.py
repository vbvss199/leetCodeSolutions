class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # so the missing values are water 
        # and if the previous jump is k then it can jump k+1 or k-1 
        # if the current jump is k then it can go k+1 or k-1 and make sure it is positive 
        # using traditional it take more steps so we store the intermediate steps 
        # [0,1,3,5,6,8,12,17]
        # [L,L,W,L,W,L,L,W,L,W,W,W,L,W,W,W,W,L]
        # given first element is 0 and first jump is 1 , so first two elements must be 0 and 1
        if(stones[1]!=1):
            return False

        # 2nd approach dont see this uncomment or comment this after trying the belopw helper funciton 
        queue=[(1,1)]
        seen=set()
        while queue:
            stone_num,k=queue.pop()
            if stone_num==stones[-1]:
                return True 
            # now search neighbours
            for nei in [k-1,k,k+1]:
                if nei<=0:
                    continue
                next_pos=stone_num+nei
                if next_pos in stones and (next_pos,nei) not in seen:
                    queue.append((next_pos,nei))
                    seen.add((next_pos,nei))
        return False
    #     return self.helper(stones,0,1)

    # def helper(self,stones,stone_number,k):
    #     # stone_number is the value of the array and k is the number of the steps taken to reach the current position 
    #      # calculate the new stone number 
    #     stone_number+=k
    #     if(stone_number)==stones[-1]:
    #         return True
    #     # check the stone number is > the arry then 
    #     if(stone_number)>stones[-1]:
    #         return False 
    #         # check if it is not in stones
    #     if stone_number not in stones:
    #         return False 

    #         # recursive condition 
    #         # check recursively with the three conditions 
    #     less=False
    #     if(k>1):
    #         less=self.helper(stones,stone_number,k-1)
    #     same=self.helper(stones,stone_number,k)
    #     more=self.helper(stones,stone_number,k+1)
    #     # return any of the sucessor
    #     return less or same or more 