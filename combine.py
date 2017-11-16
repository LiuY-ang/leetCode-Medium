# -*- coding:utf-8 -*-
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.ans=[]#用以存储结果
        self.combination(1,n,k,[])
        return self.ans
    def combination(self,start,n,k,path):#start为开始访问的位置，初始值为1；path用以存储路径
        if k==0:
            self.ans.append(path)
            return
        while start<=n:
            self.combination(start+1,n,k-1,path+[start])#改变start的值，path的值为path+[start]
            start=start+1
so=Solution()
print so.combine(4,2)
