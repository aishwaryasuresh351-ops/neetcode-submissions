class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {")": "(", "]": "[", "}": "{"}
        
        for c in s:
            if c in closetoopen:  # closing bracket
                if stack and stack[-1] == closetoopen[c]:
                    stack.pop()
                else:
                    return False
            else:  # opening bracket
                stack.append(c)
        
        return not stack  # only return after processing all characters
