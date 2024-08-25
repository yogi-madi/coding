#https://leetcode.com/problems/palindrome-number/

class Solution:
    def arm_strong(self, x: int) -> bool:
        temp = x
        ans = 0
        rem = 0
        i = 0
        while temp > 0:
            rem = temp % 10
            # print(rem,i)
            ans = ans + rem ** 3
            temp = temp // 10
            i += 1
        print(ans,x)
        return ans == x

s = Solution()
s.arm_strong(153)