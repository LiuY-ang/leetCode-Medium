# -*- coding:utf-8 -*-
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        遇到0的时候
        '''
        length=len(s)
        if length==0:
            return 0
        if s[0]=='0':
            return 0
        twoNumbers=[0]#第一个数无法构成一个两位数
        constructNumbers=[]
        if int(s[0])<1 or int(s[0])>26:#不在编码范围之内
            constructNumbers.append(0)
        else:#在编码范围之内
            constructNumbers.append(1)
        for i in range(1,length):
            print constructNumbers,twoNumbers
            if int(s[i])==0:#当前位置的数为0
                if i-2>=0:
                    constructNumbers.append(constructNumbers[i-2])
                elif int(s[i-1])>0:
                    constructNumbers.append(1)
                else:
                    constructNumbers.append(0)
                if int(s[i-1])<=2:
                    twoNumbers.append(twoNumbers[-1]+1)
                else:
                    twoNumbers.append(twoNumbers[-1])
            else:
                nearTwo=int(s[i-1:i+1])
                if  nearTwo>0 and nearTwo<10:#前一位为0,1-9
                    constructNumbers.append(constructNumbers[-1])
                    twoNumbers.append(twoNumbers[-1])
                elif nearTwo>9 and nearTwo<27:
                    if i-2>=0:
                        constructNumbers.append(constructNumbers[-1]+1+twoNumbers[i-2])
                    else:#i-1<0
                        constructNumbers.append(constructNumbers[-1]+1)
                    twoNumbers.append(twoNumbers[-1]+1)
                else:#nearTwo<=0 or nearTwo>=27
                    constructNumbers.append(constructNumbers[-1])
                    twoNumbers.append(twoNumbers[-1])
        print constructNumbers,twoNumbers
        return constructNumbers[-1]
so=Solution()
print so.numDecodings("00")
