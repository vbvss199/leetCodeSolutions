class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=len(nums1)
        n2=len(nums2)
        i=0
        j=0
        intersection=[]
        nums1.sort()
        nums2.sort()
        while((i<n1) and (j<n2)):
            # as 2is <3 so move forward there will be no partner left so we need to have a higher number i.e why we move the variable i 
            if(nums1[i]<nums2[j]):
                i=i+1
            elif(nums2[j]<nums1[i]):
                j=j+1
            elif(nums1[i]==nums2[j]):
                intersection.append(nums2[j])
                i=i+1
                j=j+1
        return list(set(intersection))