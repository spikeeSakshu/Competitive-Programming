'''
Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, 
otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. 
For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:
    Input: A = "ab", B = "ba"
    Output: true
    Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
'''


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        len_a = len(A)
        len_b = len(B)
        
        if len_a != len_b or set(A) != set(B): return False       
        if A == B:
            return len_a - len(set(A)) >= 1
        
        index = []
        for i in range(len_a):
            if A[i] != B[i]:
                index.append(i)
                if len(index) > 2:
                    return False
        if len(index) != 2:
            return False
        
        return A[index[0]]==B[index[1]] and A[index[1]]==B[index[0]]