from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group the anagrams !!
        # re arranging the words we form the words using the word atleast once so "eat" "tea" "ate" are anagarams 
        # group the words that are anagrams together , return the list of the list 
        # one thing to observe if we able to sort the chars in each. string and compare then they are anagrams !!!!
        # the TC is O(n*log(m)) where m is the length of the string and n is the length of the strings list !!!
        # lets think about the another approach ?
        # cerate a default ict which stores the key and the group anagrams 
        # and sort the first word for supose aet:[eat,tea,ate] so the sorted word matches the key append to the list with the key aet
        # anagrams_group=defaultdict(list)
        # # so we check if there is a key present if not we create the new key and append it to the list 
        # for word in strs:
        #     key="".join(sorted(word))
        #     anagrams_group[key].append(word)
        #     # and sorted(word) returns a list so convert the list to a string 
        # return list(anagrams_group.values())

        # approach 2 instead of sorting which takes the o(n*lognm) we go through the counitng approach 
        # we keep traking by the count of the 26 letters , maintain a list 0 to 25 track character for each word if it is equal at any time then push that to a lisst 
        dic=defaultdict(list)
        for word in strs:
            count=[0]*26
            for char in word:
                # ord (a) and ord(b) converts the chars to a numerical value 
                count[ord(char)-ord('a')] +=1
            # as tuples are immutable so it wont create any duplicates 
            lst=tuple(count)
            # now use this lst as key in the dic
            dic[lst].append(word)
        return list(dic.values())