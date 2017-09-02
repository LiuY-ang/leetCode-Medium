# -*- coding:utf-8 -*-
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        roman=[['I','IV','V','IX'],['X','XL','L','XC'],['C','CD','D','CM'],['M']]
        ans,base="",4
        while num!=0:
            result,i=num/pow(10,base-1),0
            if result>0 and result<=3:
                while i<result:
                    ans=ans+roman[base-1][0]
                    i=i+1
            elif result>3 and result<5: #result的结果为4
                ans=ans+roman[base-1][1]
            elif result>=5 and result<=8:
                ans=ans+roman[base-1][2]
                while i<result-5: #third大于5
                    ans=ans+roman[base-1][0]
                    i=i+1
            elif result>8:
                ans=ans+roman[base-1][3]
            num=num%pow(10,base-1)
            base=base-1
        return ans
d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
so=Solution()
print so.intToRoman(3999)
