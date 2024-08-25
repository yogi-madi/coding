# https://takeuforward.org/data-structure/print-all-divisors-of-a-given-number/

import math 

class Solution:
    def get_divisors(self, n):
        divisors = []
        sq = math.floor((math.sqrt(n)))
        for i in range(1, sq + 1):
            if n % i == 0: 
            # Add divisor i to the list
                divisors.append(i) 
                if i != n // i:
                    divisors.append(n // i)  
    # Return the list of divisors
        return divisors 

s = Solution()
print(s.get_divisors(25))
