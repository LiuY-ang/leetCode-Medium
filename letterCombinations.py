class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping={0:[" "],1:["*"],2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],
         5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
        length,self.ans=len(digits),[""]
        if length==0:
            return []
        for d in digits:
            print "d=",d
            self.combinations(mapping[int(d)])
            print "self.ans=",self.ans
        return self.ans

    def combinations(self,strlist2):
        ans=[]
        for e1 in self.ans:
            for e2 in strlist2:
                print e1+e2,
                ans.append(e1+e2)
        self.ans=ans
so=Solution()
print so.letterCombinations("22")
