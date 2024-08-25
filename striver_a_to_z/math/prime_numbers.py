# https://takeuforward.org/data-structure/check-if-a-number-is-prime-or-not/

import math 

class Solution:
    def get_divisors(self, n):
        count = 0
        sq = math.floor((math.sqrt(n)))
        for i in range(1, sq + 1):
            if n % i == 0: 
                count += 1
                 
        return count == 1 

s = Solution()
print(s.get_divisors(25))
print(s.get_divisors(11))
print(s.get_divisors(2))
print(s.get_divisors(26))
print(s.get_divisors(41))
print(s.get_divisors(97))