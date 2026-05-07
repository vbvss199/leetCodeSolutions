class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # after inserting a new array the intervals become overlapping example [1,3] [2,5] as these are overlapping so consider [1,5] and 6,9 will be the new non overlapping intervals 
        # intervals will always be in the sorted order
        # comapre the given newInterval against the intervals and divide into left an right segments and if we see the overlapping one then take the minimum and maximum kf the elements 
        # a resultant 2 d array which stores the new result 
        i=0
        result=[]
        minElement=0
        maxElement=0
        while(i<len(intervals) and intervals[i][1]<newInterval[0]):
            #find the left most and add it to the result 
            # if this condition pass then its left sub array
            result.append(intervals[i])
            i=i+1
        #find the overlapping and find the min and max and add to the result
        while(i<len(intervals) and intervals[i][0]<=newInterval[1]):
            newInterval[0]=min(intervals[i][0],newInterval[0])
            newInterval[1]=max(intervals[i][1],newInterval[1])
            i=i+1
        result.append(newInterval)
        # # find the right most array and push to result and return it ! 
        while(i<len(intervals)):
            result.append(intervals[i])
            i=i+1
        return result