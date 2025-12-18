class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1 sort the array so that all come together
        # 2 go with for loop for each arrray 
        # check them if they exists in answer array which is list of list 
        # initialise the start and end and update them

        intervals.sort()
        ans=[]
        for i in range(len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1] 
            if((len(ans)!=0)  and (end <=ans[-1][1])):
                continue
            for j in range(i+1,len(intervals)):
                if (intervals[j][0]<=end):
                    end=max(end,intervals[j][1])
                else:
                    break
            ans.append([start,end])
        return ans