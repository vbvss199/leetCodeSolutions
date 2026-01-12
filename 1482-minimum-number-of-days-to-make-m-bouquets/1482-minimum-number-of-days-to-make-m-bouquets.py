class Solution:
    def possible(self,bloomDay,day,m,k):
        # if im giving this day and along with the m and k we need to say is it possible or not !
        count=0
        n_b=0
        for i in range(len(bloomDay)):
            # for case 11 7 the day will also be considered as 7<=11
            if(bloomDay[i]<=day):
                count=count+1
            else:
                # we r in the unblooming day
                # before making it zero we need to count the number of boquets we can make 
                n_b=n_b+(count//k)
                count=0
            # tjhe abve condition number of boquets will be counted only if it is unbloomed what if the counter counts and reaches like [7 7 7 7 13 11 12 7] at 13 it breaks but if we choose 12 and the counter becomes 3 when it reches end so we need to count it again
        n_b=n_b+(count//k)
        if(n_b>=m):
            return True
        else:
            return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # lets slove this step by step
        # m= no of boquets 
        # k = no of adjacent flowers 
        # start with the minimum possible element of the array
        start_day=min(bloomDay)
        end_day=max(bloomDay)
        # naive approach
        # for j in range(start_day,end_day+1):
        #     if(self.possible(bloomDay,j,m,k)==True):
        #         return j
        # return -1

        # lets optimise the above linear loop with the binary search !!!!
        
        # optimal approach:
        answer=end_day
        if(m*k<=len(bloomDay)):
            while(start_day<=end_day):
                mid=(start_day+end_day)//2
                if(self.possible(bloomDay,mid,m,k)==True):
                    answer=mid
                    end_day=mid-1
                else:
                    start_day=mid+1
            return answer
        else:
            return -1
            