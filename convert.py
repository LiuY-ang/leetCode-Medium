class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows>=len(s) or numRows==1:
            return s
        diff=[[numRows+numRows-2,0]]
        i,length=1,len(s)
        while i<numRows:
            diff.append([diff[i-1][0]-2,diff[i-1][1]+2])
            i=i+1
        diff[0].pop()
        diff[-1].pop(0)
        print diff
        i,ans=0,""
        while i<numRows:
            step,j=0,i
            while j<length:
                print s[j],
                ans=ans+s[j]
                j=j+diff[i][step%len(diff[i])]
                step=step+1
            i=i+1
        return ans
so=Solution()
print so.convert("pa",2)
