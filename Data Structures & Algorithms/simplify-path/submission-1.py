class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        res = []

        for fragment in path.split("/"):

            if not fragment or fragment == '.': 
                continue
            elif fragment == '..':
                if stack: stack.pop()
                continue

            stack.append(fragment)
        
        return "/" + "/".join(stack)

