# -*- coding:utf-8 -*-
import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length=len(nums)
        nums.sort()
        print nums
        closest=sys.maxint
        k,i,j,ans=0,0,0,0
        while k<length:
            i,j=k+1,length-1
            print "out"
            while i<j:
                print i,j
                s=nums[k]+nums[i]+nums[j]
                if closest>abs(s-target):
                    closest=abs(s-target)
                    ans=s
                if s>target:
                    j=j-1
                elif s<target:
                    i=i+1
                elif s==target:
                    ans=0
                    return ans
            k=k+1
        return ans
so=Solution()
print so.threeSumClosest([0,2,1],3)
