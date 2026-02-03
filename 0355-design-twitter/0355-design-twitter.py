
import heapq        
class Twitter:

    def __init__(self):
        # initialisation here 
        # need to implement all the funtions
        # usage of hashmap may be for the userId and the tweetId
        # get should return the list with all the tweetId that user posted and the user following posts as well
        
        # follow and unfollow 
        # need to use hashset instead of hashmap idk why
        # this one userId ->[list of follow id's] like user 1 follows 2,3,4 then 1:[2,3,4]
        # what happens if a user unfollows him ?so searching through the entire list to find him costs O(n) time ? is there any better approach to di this ?,so the same operation can be done in O(1) time which is hashset
        
        self.followMap=defaultdict(set) #this one userId ->{set of following id's}

        # get and post methods?
        # we need to map the userId to the list of tweet id's,again a hashmap to map the userid and list of user id 's
        # the post method which can be done in O(1) time like id:add to the list at the end of the list 
        # now comes the getNewsFeed ?, for any given user the most recent tweet will be at the end of the list 
        # instead of storing list we also store the count as well for the id [count,tweetid] and may be we use min r max heap 
        self.tweetMap=defaultdict(list) #userid-> list[count,tweetId's]
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        # the 2nd item which is tweetId which we need to return based on the count 
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        # need to return the tweets which are recently posted to least posted !we track them using the count variable and min heap
        res=[]
        minHeap=[]
        # the user himself and the users he follows are in the follow map 
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            #and now the tweetmap like the count and the tweetid's
            if self.tweetMap[followeeId]:
                # lets get the index which is the last element 
                idx=len(self.tweetMap[followeeId])-1
                # this gives us the second element as we r giving length arr[][]
                count,tweetId=self.tweetMap[followeeId][idx]
                minHeap.append([count,tweetId,followeeId,idx-1])
        heapq.heapify(minHeap)
        while(minHeap and len(res)<10):
            count,tweetId,followeeId,index=heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                nextCount, nextTweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [nextCount, nextTweetId, followeeId, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        #if not default dict we need to initialise like self.followMqp[followerId]=set() 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)