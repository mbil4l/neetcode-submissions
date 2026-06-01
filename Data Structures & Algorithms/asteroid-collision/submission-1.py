class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:

            if not stack: 
                stack.append(asteroid)
                continue

            if not (asteroid < 0 and stack[-1] > 0):
                stack.append(asteroid)
            else: # asteroid is neg, stack top is pos
                while stack and stack[-1] > 0:    
                    if stack[-1] > -asteroid:
                        break
                    elif stack[-1] == -asteroid:
                        stack.pop()
                        break
                    else: # asteroid mag > stack top
                        stack.pop()
                else:
                    stack.append(asteroid)
                
                        
                
        return stack
 

        