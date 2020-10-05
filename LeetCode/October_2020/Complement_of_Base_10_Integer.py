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