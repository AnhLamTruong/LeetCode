#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right= len(nums)-1
        res=nums[0]
        while left<right:
            mid=(right+left)//2
            res=min(res,nums[mid])
            if nums[mid]>nums[right]:
                left=mid+1
                res = min(res,nums[left])
            else:
                right=mid-1
            if nums[left]<nums[right]:
                res=min(res,nums[left])
                break
        return res
                
s=Solution();
print(s.findMin([2,3,4,5,1]))
# @lc code=end

