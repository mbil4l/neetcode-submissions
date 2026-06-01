class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        midx = min(len(word1), len(word2))

        for i in range(midx):
            res.append(word1[i])
            res.append(word2[i])
        
        if len(word1) < len(word2): res.append(word2[midx:])
        else: res.append(word1[midx:])
    
        return "".join(res)

