# -*- coding:utf-8 -*-
import itertools
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        temp=sorted(nums)
        permutations=list(itertools.permutations(temp,length))
        print permutations
        numsTuple=tuple(nums)
        k=permutations.index(numsTuple)+1
        print k
        if k==len(permutations):
            k=0
        target=list(permutations[k])
        i=0
        while i<length:
            nums[i]=target[i]
            i=i+1
        print nums
so=Solution()
so.nextPermutation([1,5,1])
