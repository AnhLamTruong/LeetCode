#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
from inspect import stack


class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack=[]
        for i in str(x):
            stack.append(i)
        for i in str(x):
            tail=stack.pop()
            if tail == i:
                continue
            else:
                return False
        return True
    
s=Solution()
print(s.isPalindrome(1232321))
# @lc code=end

