#https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1

class Solution:
    def gcd(self, A, B):
        # print(A, B)
        while A > 0 and B > 0:
            if A > B:
                A = A % B
            else:
                B = B % A
            if A == 0:
                return B
        return A
        
    def lcm(self, A, B):
        gcd = self.gcd(A, B)
        return (A * B) // gcd
        
    def lcmAndGcd(self, A , B):
        # code here 
        gcd = self.gcd(A, B)
        lcm = self.lcm(A, B)
        return lcm, gcd
