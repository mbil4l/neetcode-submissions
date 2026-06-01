class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        abcdefad
        [b, c, d, e, f, a]
        
        '''
        uniqChar = set()
        l, r, res = 0, 0, 0
        
        while r < len(s):

            if s[r] in uniqChar:
                while s[r] in uniqChar:
                    uniqChar.remove(s[l])
                    l += 1
            uniqChar.add(s[r])
            res = max(r - l + 1, res)
            r += 1
        return res