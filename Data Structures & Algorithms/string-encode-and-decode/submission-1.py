class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res+= str(len(s)) + "#" + s
        return res
        
    def decode(self, strs):
        res = []
        i = 0
        while i <= len(strs) - 1:
            j = i
            while strs[j] != '#': 
                j+=1
            n = int(strs[i:j])
            res.append(strs[j+1:j+n+1])
            i = j + 1 + n
        return res









            
            
            