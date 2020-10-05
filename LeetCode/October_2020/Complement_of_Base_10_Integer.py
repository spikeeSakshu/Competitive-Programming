'''
Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

 
Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
'''

class Solution:
    def binaryToDecimal(self, N):
        return int(N, 2)
               
    def decimalToBinary(self, N, binary):
        if N>1:
            self.decimalToBinary(N//2, binary)
        
        binary.append(N%2)
        
        return binary, ''.join([str(int(not(i))) for i in binary])
            
        
    def bitwiseComplement(self, N: int) -> int:
        
        binary, twos_complement= self.decimalToBinary(N, [])
        decimal= self.binaryToDecimal(twos_complement)
        
        return decimal        
        
if __name__ == '__main__':
    s= Solution()
    print(s.bitwiseComplement(5))