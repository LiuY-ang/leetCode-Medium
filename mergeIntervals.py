# -*- coding:utf-8 -*-
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        length=len(intervals)
        if length==0:
            return []
        if length==1:
            return intervals
        def compared(a,b):#定义对Interval的排序规则
            if a.start>b.start:#首先按照开始时间排序，开始时间早的，排序靠前
                return 1
            elif a.start<b.start:#开始时间晚的，排序靠后
                return -1
            else:#a.start==b.start，如果开始时间相同，那么比较结束时间
                if a.end>b.end:#结束时间晚，排序靠后
                    return 1
                elif a.end<b.end:#结束时间早，排序靠前
                    return -1
                else:#开始时间和结束时间相同的情况
                    return 0
        sortedIntervals=sorted(intervals,compared)#排序
        i,ans=1,[]#从第一个元素开始，ans用于存储结果
        latestEndTime=sortedIntervals[0].end#latestEndTime存储为最晚的结束时间，初始化为第一个元素的结束时间
        earlyStartTime=sortedIntervals[0].start#最早的开始时间，初始化为第一个元素的开始时间
        while i<length:#i从1开始
            if sortedIntervals[i].start==sortedIntervals[i-1].start and sortedIntervals[i].end==sortedIntervals[i-1].end:#去除重复元素
                if i==length-1:#如果i在最后一个位置上
                    ans.append([earlyStartTime,latestEndTime])#将可能丢失的位置信息添加
                i=i+1
                continue
            if sortedIntervals[i].start>latestEndTime:#如果某段区间的开始时间大于已知的最晚结束时间，那么就已经没有重叠的时间段了
                ans.append([earlyStartTime,latestEndTime])#将已知的开始最早开始时间，最晚结束时间添加到ans中
                #更新earlyStartTime,latestEndTime
                earlyStartTime,latestEndTime=sortedIntervals[i].start,sortedIntervals[i].end
            elif sortedIntervals[i].end>=latestEndTime:#如果latestEndTime在某一个区间的内部
                latestEndTime=sortedIntervals[i].end#那么证明有重叠部分，更新latestEndTime,即最晚结束时间
            if i==length-1:#检测i是否在最后位置上，以免漏掉区间信息
                ans.append([earlyStartTime,latestEndTime])
            i=i+1
        return ans
so=Solution()
i2=Interval(1,7)
i1=Interval(1,6)
i3=Interval(8,10)
i4=Interval(15,18)
i=[i1,i2]
print so.merge(i)
