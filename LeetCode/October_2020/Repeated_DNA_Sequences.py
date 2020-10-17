'''
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example 1:

    Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

    Input: s = "AAAAAAAAAAAAA"
    Output: ["AAAAAAAAAA"]
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        
        sequences= {}
        result= []

        for i in range(len(s)-9):
            seq= s[i:i+10]

            if seq not in sequences:
                sequences[seq] =1
            else:
                sequences[seq]+=1
        
        for key in sequences:
            if sequences[key]!=1:
                result.append(key)
                
        return result            
        