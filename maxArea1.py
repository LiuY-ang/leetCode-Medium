# -*- coding:utf-8 -*-
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length,max_area=len(height),0
        i,j,pos=0,length-1,{}
        while i<j:
            max_area=max((j-i)*min(height[i],height[j]),max_area)#取得最大值
            #较大的高度保持位置不变，改变较小的高度
            if height[i]>height[j]:
                j=j-1
            else:
                i=i+1
        return max_area
so=Solution()
print so.maxArea([1,8, 6, 2, 5, 4, 8, 3, 7])
