class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1: return False

        stack = []

        mapping = {']':'[', '}':'{', ')':'('}

        for char in s:

            if stack and char in {']', '}', ')'}:

                if stack[-1] != mapping[char]: return False
                else: stack.pop()
                
            else:

                stack.append(char)

        return len(stack) == 0