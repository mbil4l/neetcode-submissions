class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for idx, char in enumerate(s):

            if char == "]":

                testString = []

                while stack and stack[-1] != "[":

                    testString.append(stack.pop())
                
                stack.pop() # [

                multiplier, factor = 0, 1

                while stack and stack[-1].isnumeric():

                    multiplier += int(stack.pop()) * factor
                    factor *= 10

                testString.reverse()
                
                st = "".join(multiplier * testString)

                stack.append(st)

            else:
                stack.append(char)
        
        return "".join(stack)

        