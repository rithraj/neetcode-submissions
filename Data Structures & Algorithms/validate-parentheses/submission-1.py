class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "}":"{","]":"["}

        stack = []

        for c in s:
            if c in mapping:
                if len(stack) > 0:
                    char = stack.pop()
                else:
                    return False
                    
                if char == mapping[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        else:
            return False
            

        