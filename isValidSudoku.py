# -*- coding:utf-8 -*-
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m,n=9,9
        #[[0]*n for i in range(n)]
        rows=[[] for i in range(m)]
        columns=[[] for i in range(n)]#会分配相同的地址
        for i in range(n):#检查第一行
            if board[0][i] in rows[0]:
                return False
            elif board[0][i]!='.':  #跳过'.'
                rows[0].append(board[0][i])#添加到行中
                # columns[i].append(board[0][i])#也需要添加到列中
        print rows,"   ",columns
        for j in range(1,m):#检查第一列
            if board[j][0] in columns[0]:#如果有重复的话
                return False
            elif board[j][0]!='.':
                columns[0].append(board[j][0])#添加到第一列中的元素
                rows[j].append(board[j][0])
        print rows,"  ",columns
        #经过上边检查完第一行和第一列之后，执行的这里，说明第一行和第一列中没有重复的元素
        i,j=1,1
        while i<m:
            j=1
            while j<n:
                # print i,j,'*'
                if board[i][j] in rows[i]: #检查行中的元素
                    return False
                elif board[i][j]!='.':#行中的元素不存在该元素
                    rows[i].append(board[i][j])
                if board[i][j] in columns[j]:#检查列中元素
                    return False
                elif board[i][j]!='.':#列中不存在该元素，则将该元素添加进去
                    columns[j].append(board[i][j])
                j+=1
            i+=1
        #检查小9格
        print rows
        print columns
        return True
so=Solution()
print so.isValidSudoku(["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"])
