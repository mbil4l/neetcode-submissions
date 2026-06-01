class Solution:
    def trap(self, heights: List[int]) -> int:

        prefix = [0] * len(heights)
        suffix = [0] * len(heights)

        pre = 0
        for h in range(len(heights) - 1):
            if heights[h + 1] < heights[h]: 
                pre = max(pre, heights[h])
            prefix[h] = pre    
        
        suf = 0
        for s in range(len(heights) - 1, 0, -1):
            if heights[s - 1] < heights[s]: 
                suf = max(suf, heights[s])
            suffix[s] = suf    
                
        print(prefix)
        print(suffix)

        water = 0

        for i in range(len(heights)):
            cur = min(prefix[i], suffix[i]) - heights[i]
            water += cur if cur > 0 else 0
        
        return water
        

        
        


        

            




        