class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1 sort the array so that all come together
        # 2 go with for loop for each arrray 
        # check them if they exists in answer array which is list of list 
        # initialise the start and end and update them

        intervals.sort()
        ans=[]
        # better approach
        # for i in range(len(intervals)):
        #     start=intervals[i][0]
        #     end=intervals[i][1] 
        #     if((len(ans)!=0)  and (end <=ans[-1][1])):
        #         continue
        #     # fix the first element and go check with the remaining whether they r overlapping or not 
        #     for j in range(i+1,len(intervals)):
        #         # just like (1,3) (2,4). so below checks 2<=3, so 4 gets replaced by 3 in the ans 
        #         if (intervals[j][0]<=end):
        #             end=max(end,intervals[j][1])
        #         else:
        #             break
        #     ans.append([start,end])
        # return ans

        # optimal approach 
        n=len(intervals)
        for i in range(n):
            # we need to add anew interval to the ans list if there is nothing so 
            # condition for pushing new interval to the ans list like (1,6) and (8,9) we need to push 8,9 
            if( (len(ans)==0) or (intervals[i][0] > ans[-1][1]) ):
                # push the interval so the initial interval (1,3) goes in 
                ans.append(intervals[i])
            # what if it is not greater so we need to update the interval 
            else:
                # start comparing (1,3) and (2,4)
                # we need to replace 1,3 to 1,4 
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
        return ans