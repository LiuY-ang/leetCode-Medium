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
                    if self.detectWord(i,j,board,word,0):
                        return True
        return False
    def detectWord(self,row,column,board,word,pos):
        if pos==len(word):
            return True
        if row<0 or row>=len(board) or column<0 or column>=len(board[0]) or word[pos]!=board[row][column]:
            return False
        temp=board[row][column]
        board[row][column]="#"
        result=self.detectWord(row-1,column,board,word,pos+1) or self.detectWord(row+1,column,board,word,pos+1) \
            or self.detectWord(row,column-1,board,word,pos+1) or self.detectWord(row,column+1,board,word,pos+1)
        board[row][column]=temp
        return result
so=Solution()
print so.exist([
  ['a'],
],"ab")
