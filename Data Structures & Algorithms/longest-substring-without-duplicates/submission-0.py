class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        uniqChar = set()
        l, r, res = 0, 0, 0
        
        while r < len(s):

            if s[r] not in uniqChar:
                uniqChar.add(s[r])
            else:
                while s[r] in uniqChar:
                    uniqChar.remove(s[l])
                    l += 1
                uniqChar.add(s[r])
            r += 1
            res = max(len(uniqChar), res)
        return res
