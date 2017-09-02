# -*- coding:utf-8 -*-
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans=[]
        length=len(candidates)
        candidates.sort()#排序
        self.visitElements(candidates,[],target,length,0)
        return self.ans
    def visitElements(self,candidates,path,target,length,i):#path用于存储路径
        if target<0:
            return
        if target==0:
            if path not in self.ans:#防止有重复的元素
                self.ans.append(path)
            return
        while i<length:
            if candidates[i]>target: #此时的target已经变了,以前写的是if candidates[i]>target and sum(path)>target
                return#并不能得到正确的结果，所以改变写法。如果candidates[i]>target,继续递归后target小于0
            self.visitElements(candidates,path+[candidates[i]],target-candidates[i],length,i+1)
            i=i+1
so=Solution()
print so.combinationSum2([1,2,2,2,5],5)
