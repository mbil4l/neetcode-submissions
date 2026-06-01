class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] 
        res = [0] * len(temperatures)
        

        for idx, temp in enumerate(temperatures): 

            if not stack:
                stack.append(idx)
                continue
            
            while stack and temp > temperatures[stack[-1]]:
                res[stack[-1]] = idx - stack[-1]
                stack.pop()
            else:
                stack.append(idx)
        
        return res

