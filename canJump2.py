# -*- coding:utf-8 -*-
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxSteps=[nums[0]]#在第一个位置能够跳跃的最大步数为第一个元素值
        length=len(nums)
        for i in range(1,length):#
            maxStep=max(maxSteps[i-1],nums[i-1])-1#maxStep是在当前位置i还能跳跃的最大步数，
            #它的值为前一个元素和历史上最大元素的值减1,它和本位置的值无关。如果在本位置的maxStep的值
            #为0，那么在下一个位置检查是否能够到达最后
            if maxStep<0:#如果在当前位置能够跳跃的最大步数为负数那么无法到达最后
                return False
            maxSteps.append(maxStep)
        return True
so=Solution()
print so.canJump([0,1])
