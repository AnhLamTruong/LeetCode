#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
# O(n)
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Hash Map implementaption 
        # hash={}
        # newArray=[]
        # for i,n in enumerate(nums):
        #     if (n not in hash):
        #         newArray.append(n)
        #         hash[n]=i
        # return len(newArray)
        
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:      
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i] 
                # Incrementing insertIndex count by 1 
                insertIndex = insertIndex + 1
        return insertIndex
    
s=Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
                
            
# @lc code=end

