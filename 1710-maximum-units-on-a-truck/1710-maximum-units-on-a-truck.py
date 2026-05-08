class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # first things first pick up the box which has the maximum units first ? correct or wrong no 
        # so instead try to pick the one which gives the max for a unit 
        # so first box 1 box 3 units , 2nd 1 box two unit per one box , 3rd 3 boxes 1 unit each so pick accordingly !!!!!
        # so first box 3 units second box one unit and thirs box one unit 
        # so think greedily to pick them like 3 units first 1unit nec t and one unit next 
        # finding the number of units per each box like boxes/units 
        # steps
        # figure out the ratio and sort in the descending order then done and dusted !
        
        # 1. sort the array according to the ratios or compaator! using sort in place use sort if some other then sorted 
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        total_val=0
        for i in range(len(boxTypes)):
            if boxTypes[i][0]<=truckSize:
                total_val=total_val+boxTypes[i][0]*boxTypes[i][1]
                truckSize=truckSize-boxTypes[i][0]
            else:
                # take only what we can fit the truck 
                total_val=total_val+truckSize*boxTypes[i][1]
                break
        return total_val

        return total_val