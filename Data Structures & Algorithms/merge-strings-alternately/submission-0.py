class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ''
        midx = min(len(word1), len(word2))

        for i in range(midx):
            res += f"{word1[i]}{word2[i]}"
        
        if len(word1) < len(word2): res += word2[midx:]
        else: res += word1[midx:]
    
        return res

