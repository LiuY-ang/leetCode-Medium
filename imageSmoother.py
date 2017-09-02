# -*- coding:utf-8 -*-
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        i,length=0,len(M)
        ans=[]
        while i<len(M):
            j,row=0,[]
            while j<len(M[i]):
                #依次检查上下左右
                s,points=0,0
                if M[i][j]!=0:
                    s+=M[i][j]
                if i-1>=0:#上
                    s+=M[i-1][j]
                    points+=1
                if i+1<length:#下
                    s=s+M[i+1][j]
                    points+=1
                if j-1>=0:#左
                    s=s+M[i][j-1]
                    points+=1
                if j+1<len(M[i]):#右
                    s=s+M[i][j+1]
                    points+=1
                if i-1>=0 and j-1>=0:#左上
                    s=s+M[i-1][j-1]
                    points+=1
                if i-1>=0 and j+1<len(M[i]):#右上
                    s=s+M[i-1][j+1]
                    points+=1
                if i+1<length and j-1>=0:#左下
                    s=s+M[i+1][j-1]
                    points+=1
                if i+1<length and j+1<len(M[i]):#右下
                    s=s+M[i+1][j+1]
                    points+=1
                print "s=",s,"points=",points+1,1.0*s/(points+1)
                row.append(int(1.0*s/(points+1)))
                j=j+1
            ans.append(row)
            i=i+1
        return ans
so=Solution()
print so.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])
