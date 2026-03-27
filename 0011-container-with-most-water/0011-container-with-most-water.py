class Solution:
    def maxArea(self, height: List[int]) -> int:
        # water will be stored in the shorter line as if there are two heights 6,8 we consider the minimum as it is useless to consider the height 8 as water gets stored till the shorter height 
        # so consider height using min(h1,h2) and are it is constant always between the pointers h1 and h2
        # consider two pointers and start shrinking 
        left=0
        max_area=0
        right=len(height)-1
        while(left<right):
            area=min(height[left],height[right])*(right-left)
            if area>max_area:
                max_area=area
            if(height[left]<height[right]):
                left=left+1
            else:
                right=right-1
        return max_area
            