# -*- coding:utf-8 -*-
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        i=length-2
        #finding first decreasing element
        while i>=0 and nums[i]>=nums[i+1]:
            i=i-1
        print "i=",i
        if i==-1:
            nums.sort()
        else:
            j=i+1
            while j<length and nums[j]>nums[i]:
                j=j+1
            j=j-1
            print i,j
            nums[i],nums[j]=nums[j],nums[i]#swap
            reverse=nums[i+1:][::-1]
            k=0
            while k<len(reverse):
                nums[k+i+1]=reverse[k]
                k=k+1
        return nums
so=Solution()
print so.nextPermutation([5,1,1])
