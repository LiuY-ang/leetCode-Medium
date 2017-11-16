# -*- coding:utf-8 -*-
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        i=0
        if x==1.0 or n==0:#如果x为1或者n为0，那么多少次幂都是1，
            return 1.0
        nisNagetive=False#标记n是否为负数
        if n<0:#n为负数的情况
            n=-n
            nisNagetive=True
        xisNagetive=False#标记x是否为负数
        if x<0 and n%2==1:#如果x为负数且n为奇数，那么结果为负数
            x=-x
            xisNagetive=True
        s,count=x,1#s初始化为x的一次幂；count表示x的几次幂
        while count<n:#主要为了减小循环次数
            s=s*s
            count=count+count
        s=s/pow(x,count-n)#将多乘的幂再除掉
        if nisNagetive:#如果为负数
            return 1/s
        elif xisNagetive:#x为负数，且n为奇数
            return -s
        return s
so=Solution()
print so.myPow(0.22838,7)
