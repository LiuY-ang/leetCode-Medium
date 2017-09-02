# -*- coding:utf-8 -*-
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans=[]#存储答案
        candidates.sort()#排序，以便减少递归的深度
        self.dfs(candidates,target,0,[])
        return self.ans
    def dfs(self,nums,target,index,path):#path用以存储路径
        if target==0:#如果此时target等于0，说明此时path之和为target
            self.ans.append(path)#则将path添加到self.ans中
            return#结束递归
        if target<0:#如果此时target小于0，则继续递归下去target只会越来越小，
            return#那么结束递归
        for i in range(index,len(nums)):
            if nums[i]>target:#主要用于减少递归的深度
                break
            self.dfs(nums,target-nums[i],i,path+[nums[i]])#这是最关键的地方，需要理解
so=Solution()
print so.combinationSum([2,3,5],10)
