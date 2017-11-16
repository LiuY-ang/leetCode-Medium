# -*- coding:utf-8 -*-
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length=len(nums)
        if length==1:
            return [[]]+[nums]
        ans=[[i] for i in nums]+[nums]+[[]]
        for i in range(2,length):
            self.temp=[];path=[]
            self.combination(nums[:],0,i,path)
            ans+=self.temp
        return ans
    def combination(self,numbers,start,k,path):#start为开始访问的位置，初始值为1；path用以存储路径
        if k==0:
            self.temp.append(path)
            return
        while start<len(numbers):
            self.combination(numbers,start+1,k-1,path+[numbers[start]])
            start=start+1
so=Solution()
print so.subsets([0])
