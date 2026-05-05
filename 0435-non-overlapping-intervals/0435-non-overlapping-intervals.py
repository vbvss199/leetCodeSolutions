class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # as said if they touch at one point they said to be non overlapping !
        # interval =starting,ending 
        # we need to remove the number of the intervals so that they will be overlapping 
        # as in the first case 1,3 is overlapping with the three of them so if we remove them then the remaining three intervals will be non overlapping 
        # thw question is we need to remove the minimum intervals 
        # prerequisite is the number of meetings that we can accomodidate in the given room 
        # same problem like the above one but count the meetings that we accomidate then remove it from the total intervals thats it 
        # sort based on the end timing 
        intervals.sort(key=lambda x:x[1])
        count=1
        meeting_free_time=intervals[0][1]
        for i in range(1,len(intervals)):
            if(intervals[i][0]>=meeting_free_time):
                count=count+1
                meeting_free_time=intervals[i][1]
        return len(intervals)-count