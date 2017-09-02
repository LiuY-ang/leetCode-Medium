# -*- coding:utf-8 -*-
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans=[]#存储答案
        self.generate("",n,n)
        return self.ans
    def generate(self,path,left,right):#path存储路径，left代表左括号，right代表右括号
        if left!=0:#左括号还有剩余
            self.generate(path+"(",left-1,right)
        if right>left:#右括号大于左括号，
            self.generate(path+")",left,right-1)
        if not right:#右括号已经匹配完，代表左括号，右括号都已经匹配完
            self.ans.append(path)
so=Solution()
print so.generateParenthesis(3)
