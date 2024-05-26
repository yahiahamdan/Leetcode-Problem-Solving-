       
"""
this is o(n) soltuion the brute force solution
"""
def containerWithMostWater(nums,height):
        left=0 
        right =len(height)-1
        areaMax=0
        while left <right:
            area=(right-left) * min(height[right],height[left])
            areaMax= max(area,areaMax)
            if height[right]<height[left]:
                right-=1
            else :
              left+=1
        return areaMax
def containerWithMostWaterBrute(nums,height):
        maxArea=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                area= (j-i) * min(height[j],height[i])
                maxArea=(maxArea,area)
        return maxArea