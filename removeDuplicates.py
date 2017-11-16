class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        pre,length=nums[0]-1,len(nums)
        count=0;i=0
        while i<len(nums):
            print i,count,len(nums)
            if nums[i]==pre:
                count=count+1
            else:#nums[i]!=pre
                pre=nums[i]
                count=1
            if count>2:
                nums.pop(i)
                print len(nums)
                i-=1
                count-=1
            i=i+1
        print nums
        return len(nums)
so=Solution()
print so.removeDuplicates([1,1,1,1])
