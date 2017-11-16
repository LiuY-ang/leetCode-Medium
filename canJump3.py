# -*- coding:utf-8 -*-
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxDistance=0#maxDistance存储为最远能够到达的位置
        length=len(nums)
        for i in range(length):
            if i>maxDistance or i>=length-1:#如果i>=length-1代表着一定能够到达最后一个位置
                break#如果i>maxDistance,最远距离maxDistance到达不了i所在的位置，即无法跨过maxDistance所在的位置
            maxDistance=max(maxDistance,i+nums[i])#保存最远能够到达的距离
        return maxDistance>=length-1
so=Solution()
print so.canJump([0,2,3])
