#https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        ans = 0
        rem = 0
        i = 0
        while temp > 0:
            rem = temp % 10
            # print(rem,i)
            ans = (ans * 10 )+ rem
            temp = temp // 10
            i += 1
        # print(ans,x)
        return ans == x