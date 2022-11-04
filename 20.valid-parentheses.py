#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            # if(i == ')' and stack.pop()!='('):
            #     return False
            # if(i == ']' and stack.pop()!='['):
            #     return False
            # if(i == '}' and stack.pop()!='{'):
            #     return False
            
            if (stack and (i==')' or i==']' or i=='}')):
                if(i == ')' and stack.pop()!='('):
                    return False
                if(i == ']' and stack.pop()!='['):
                    return False
                if(i == '}' and stack.pop()!='{'):
                    return False
            else:
                stack.append(i)
                
        if stack:
            return False
        else:
            return True
    
s=Solution()
print(s.isValid("]"))
        
# @lc code=end

