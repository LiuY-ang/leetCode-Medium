# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length,p=0,head
        while p:#该循环得到链表的长度
            p=p.next
            length=length+1
        print length
        if length==0:#如果链表长度为0，即head==None，那么返回空list
            return []
        k=k%length#k有可能会超过length，所以用k对length取余
        if k==0:#如果k==0，返回原链表即可
            return head
        i,fast=0,head#设置一个快指针fast，让其从第一个节点开始先走k个节点
        while i<k:
            fast=fast.next
            i=i+1
        p=head#然后在设置一个指针p，然后指针p和fast一起往前走
        while fast.next!=None:#fast在最后一个节点的时候停下，此时fast和p分别指向最后一个节点，
            p=p.next#p指向第length-k个节点
            fast=fast.next
        ans=p.next#保存需要返回的节点
        fast.next=head#分别改变fast和p的指向即可
        p.next=None
        return ans
