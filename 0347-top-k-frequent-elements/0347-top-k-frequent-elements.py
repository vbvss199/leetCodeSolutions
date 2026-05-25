class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # save the number and the freq in the hashmap and return the k results from the hashmap 
        freqMap={}
        for i in range(len(nums)):
            if nums[i] in freqMap:
                freqMap[nums[i]]+=1
            else:
                freqMap[nums[i]]=1
        # freqMap is built now return the k most frequent elements weneed to return the keys

        # before that sort based on the frequency
        sorted_freqMap=sorted(freqMap,key=freqMap.get,reverse=True)
        return sorted_freqMap[:k]