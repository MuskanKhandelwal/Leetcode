class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Brute force
        # maxArea = 0 
        # for i in range (len(heights)):
        #     for j in range (i+1,len(heights)):
        #         area = (j-i) * min(heights[i],heights[j])
        #         maxArea = max(maxArea, area)
        # print (maxArea)
        # return maxArea
        # optimized
        l,r = 0 , len(heights) - 1
        Maxarea = 0
        while l<r:
            area = (r-l) * min(heights[r],heights[l])
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
            Maxarea = max(Maxarea, area)
        return Maxarea
