class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # we need to return the minimum weight capacity the ship can ship in asingle day
        # the minimum weight the ship should accomodidate is atleast the maximum of the weights so 
        # the mim gonna be max(weights) and max will be the sum of the weights 
        # so we try every weights that can be accomidated each day from min to max 
        # the range is in between min and max
        # function which calculte the number of the days
        def calculate_days(weights: List[int],capacity:int) -> int:
            # we start at day 0 and load 0
            day=1
            load=0
            for i in range(0,len(weights)):
                # now we need to add and comapre against the capacity 
                if(load+weights[i]>capacity):
                    day=day+1
                    load=weights[i]
                else:
                    load+=weights[i]
            return day

        # for capacity in range(max(weights),sum(weights)+1):
        # # send this capacity along the weights which calcualte the days 
        # num_of_days=calculate_days(weights,capacity)
        # # now define the calculate_days function !!!
        # if(num_of_days<=days):
        #     return capacity 
        # lets replace the above code of line with the binary search instead of searching everything
        low=max(weights)
        high=sum(weights)
        while(low<=high):
            mid=(low+high)//2
            if(calculate_days(weights,mid)<=days):
                high=mid-1
            else:
                low=mid+1
        return low

                    
            