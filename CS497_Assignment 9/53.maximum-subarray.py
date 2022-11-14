#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr=[]
        arr.append(nums[0])
         # Initialize the max sum...
        maxSum = arr[0]
        for i in range(1,len(nums)):
            arr.append(max(arr[i-1] + nums[i], nums[i]))
            if arr[i] > maxSum:
                maxSum=arr[i]
        return maxSum
# @lc code=end

s=Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
