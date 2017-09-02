class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        if target>=nums[0]:
            i=0
            while i+1<len(nums) and nums[i]<nums[i+1]:
                if nums[i]==target:
                    return i
                i=i+1
            if nums[i]==target:
                return i
            return -1
        elif target<=nums[-1]:
            i=len(nums)-1
            while i>0 and nums[i-1]<nums[i]:
                if nums[i]==target:
                    return i
                i=i-1
            if nums[i]==target:
                return i
            return -1
        return -1
so=Solution()
print so.search([3,1],2)
