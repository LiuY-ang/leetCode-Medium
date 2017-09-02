class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length,m,n=len(nums),0,0
        nums.sort()
        ans=[]
        print nums
        while m<length:
            n=m+1
            while n<length:
                i,j=n+1,length-1
                # if n+1<length and nums[n]==nums[n+1]:
                #     n=n+1
                #     continue
                while i<length and j>n and i<j:
                    print m,n,i,j
                    s=nums[m]+nums[n]+nums[i]+nums[j]
                    if s==target:
                        row=[nums[m],nums[n],nums[i],nums[j]]
                        if row not in ans:
                            ans.append(row)
                        i,j=i+1,j-1
                    elif s>target:
                        j=j-1
                    elif s<target:
                        i=i+1
                n=n+1
            m=m+1
        return ans
so=Solution()
print so.fourSum([0,0,0,0],0)
