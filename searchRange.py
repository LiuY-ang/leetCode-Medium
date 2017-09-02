class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        possible=self.binarySearch(nums,0,len(nums)-1,target)
        if possible==-1:
            return [-1,-1]
        i,j=possible,possible
        while j<len(nums) and nums[j]==nums[possible]:
            j=j+1
        while i>=0 and nums[i]==nums[possible]:
            i=i-1
        return [i+1,j-1]
    def binarySearch(self,nums,low,high,target):
        if low<=high:
            mid=(low+high)/2
            # print low,high,mid
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return self.binarySearch(nums,low,mid-1,target)
            elif nums[mid]<target:
                return self.binarySearch(nums,mid+1,high,target)
        return -1
so=Solution()
print so.searchRange([5,7,7,8,8,10],1)
