#User function Template for python3
# https://www.geeksforgeeks.org/problems/count-digits5716/1

class Solution:
    def evenlyDivides (self, N):
        # code here
        count = 0
        temp =  N
        while N > 0:
            rem = N % 10
            # print(rem, temp)
            if rem != 0 and temp % rem == 0:
                count += 1
            N = N // 10
        return count
            
s = Solution()
print(s.evenlyDivides(2446) == 1)