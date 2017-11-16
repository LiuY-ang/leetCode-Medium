# -*- coding:utf-8 -*-
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length=len(nums)
        i=0
        one,two=nums[:],nums[:]
        while i<length-1:
            if nums[i]>nums[i+1]:
                one[i]=nums[i+1]
                two[i+1]=nums[i]
                break
            i=i+1
        print i,one,two
        def valid(array,i):
            while i<length-1:
                if array[i]>array[i+1]:
                    return False
                i=i+1
            return True
        return valid(one,i-1) or valid(two,i-1)
so=Solution()
print so.checkPossibility([3,4,2,3])
