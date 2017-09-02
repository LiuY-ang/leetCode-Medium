# -*- coding:utf-8 -*-
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        abcd=[A,B,C,D]
        self.count=0
        self.preCount=0
        return self.visitIndex(abcd,[],0,[])
    def visitIndex(self,abcd,path,depth,pathSum):#path存储路径，pathSum存储路径上的值，depth用来存储即将要访问的数组
        if depth<=3:
            i,pre,now=0,0,0
            while i<len(abcd[depth]):
                if i>0 and abcd[depth][i]==abcd[depth][i-1]:#这句话不严谨
                    print depth,i,now,pre
                    now=now+pre
                    print "now=",now
                else:
                    pre=now
                    now+=self.visitIndex(abcd,path+[i],depth+1,pathSum+[abcd[depth][i]])
                    pre=now-pre
                i=i+1
            return now#统计完某一层之后，返回本层的结果
        if depth==4 and sum(pathSum)==0:
            print "path=",path,"pathSum=",pathSum
            return 1
        return 0
so=Solution()
print so.fourSumCount([0,1,-1],
[-1,1,0],
[0,0,1],
[-1,1,1])
