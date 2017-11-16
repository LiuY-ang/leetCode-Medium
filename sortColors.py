# -*- coding:utf-8 -*-
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,left=0,0;right=len(nums)-1
        while left<=right:
            if nums[left]==0:#需要将该元素放到最前面
                nums[i],nums[left]=nums[left],nums[i]
                left,i=left+1,i+1
            elif nums[left]==1:#当前元素为1，不进行元素的移动
                left=left+1
            else:#即nums[left]==2,需要将该元素放到最后面
                nums[left],nums[right]=nums[right],nums[left]
                right=right-1
        print nums
so=Solution()
print so.sortColors([1,1,1,2,2,2,0,0])
