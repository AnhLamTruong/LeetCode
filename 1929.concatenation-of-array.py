#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#
from typing import List

# @lc code=start
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newArray=[]
        for i in range(len(nums)):
            newArray.append(nums[i])
        for i in range(len(nums)):
            newArray.append(nums[i])
        return newArray
            
            
s=Solution()
print(s.getConcatenation([1,3,2,1]))
# @lc code=end

