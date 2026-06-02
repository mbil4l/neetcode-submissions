class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        first, second = [0] * 26, [0] * 26

        for i in range(len(s)):
            first[ord(s[i]) - ord('a')] += 1
            second[ord(t[i]) - ord('a')] += 1
        
        return first == second


        