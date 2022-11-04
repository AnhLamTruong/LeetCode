#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List 
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size=len(nums)
        insertValue=0
        for i in range(0,size):
            if (nums[i] != val):
                nums[insertValue]=nums[i]
                insertValue=insertValue+1
        return insertValue;
            
        
# @lc code=end

