'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

'''

class Solution:
    def removeDuplicateLetters(self, text: str) -> str:
        if not text:
            return ''
        import collections
        freq_map = collections.Counter(text)
        used = [False]*26
        result = ''
        for char in text:
            freq_map[char] -= 1
            if used[ord(char)-97]:
                continue
            while (result and result[-1] > char and freq_map[result[-1]] > 0):
                used[ord(result[-1])-97] = False
                result = result[:-1]
            used[ord(char)-97] = True
            result += char
        return result