# -*- coding:utf-8 -*-
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length,d,ans=len(nums),{},[]
        i,j,k=0,0,0
        nums.sort()
        print "nums=",nums
        for i in xrange(len(nums)-1):
            print "nums[%d]=%d" % (i,nums[i]),
            if i>0 and nums[i]==nums[i-1]:#去除重复元素
                continue
            low,high=i+1,length-1
            print "low=",low,"high=",high
            while low<high:
                s=nums[low]+nums[high]+nums[i]
                if s>0:
                    high=high-1
                elif s<0:
                    low=low+1
                else:
                    ans.append([nums[i],nums[low],nums[high]])
                    target,low=nums[low],low+1
                    while low<length and nums[low]==target:#避免超出界线和重复元素
                        low=low+1
                    target,high=nums[high],high-1
                    while high>=0 and nums[high]==target:#避免重复元素
                        high=high-1
        return ans#如何避免重复的元素
so=Solution()
print so.threeSum([0,0,0])
