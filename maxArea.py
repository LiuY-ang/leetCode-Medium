# -*- coding:utf-8 -*-s
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j,length,max_area=0,0,len(height),0
        while i<length:
            j=i+1
            while j<length:
                if (j-i)*min(height[j],height[i])>max_area:
                    max_area=(j-i)*min(height[j],height[i])
                j=j+1
            i=i+1
        return max_area
so=Solution()
print so.maxArea([1,8, 6, 2, 5, 4, 8, 3, 7])
