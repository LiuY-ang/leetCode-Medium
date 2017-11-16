# -*- coding:utf-8 -*-
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        visited=[]
        m,n=len(board),len(board[0])
        length=len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:#第一个元素相等
                    # visited.append([i,j])
                    if self.detectWord(i,j,board,word,0,visited):
                        return True
        return False
    def detectWord(self,row,column,board,word,pos,visited):
        if pos<len(word) and board[row][column]==word[pos]:
            visited.append([row,column])
            if pos==len(word)-1:#最后一个元素也存在了
                # print "last step!"
                return True
            up,down,left,right=False,False,False,False
            if row>0 and [row-1,column] not in visited:#待访问的坐标不在已访问过的集合中
                up=self.detectWord(row-1,column,board,word,pos+1,visited)
            if row+1<len(board) and [row+1,column] not in visited:
                down=self.detectWord(row+1,column,board,word,pos+1,visited)
            if column-1>=0 and [row,column-1] not in visited:
                left=self.detectWord(row,column-1,board,word,pos+1,visited)
            if column+1<len(board[0]) and [row,column+1] not in visited:#打算往右走，前一步不能从右边来
                right=self.detectWord(row,column+1,board,word,pos+1,visited)
            visited.pop()
            return up or down or left or right
        return False
so=Solution()
print so.exist([
  ['a','a','a','a'],
  ['a','a','a','a'],
  ['a','a','a','a'],
],"aaaaaaaaaaaa")
