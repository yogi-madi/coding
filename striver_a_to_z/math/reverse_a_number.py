# https://leetcode.com/problems/reverse-integer/
import math 

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1      # 2,147,483,647
        INT_MIN = -2**31         #-2,147,483,648
        reverse = 0

        while x!=0:
            if reverse > INT_MAX/10 or reverse < INT_MIN/10 :
                return 0
            elif x>0:
                digit = x % 10
                reverse = reverse * 10 + digit
                x=math.trunc(x/10)
            else:
                digit = x % -10
                reverse = reverse * 10 + digit
                x=math.trunc(x/10)  
        return reverse   
     
s = Solution()
print(s.reverse(2345) == 5432)
print(s.reverse(-2345) == -5432)