class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        candidate = [0] * 26
        current = [0] * 26

        for char in s1:
            candidate[ord(char) - ord('a')] += 1
        
        n = len(s1)

        for i in range(len(s2)):

            if i < n:
                current[ord(s2[i]) - ord('a')] += 1
            else:
                current[ord(s2[i - n]) - ord('a')] -= 1
                current[ord(s2[i]) - ord('a')] += 1
            
            if current == candidate: return True
        
        return False
                






        