class Solution:
    def isValid(self, s: str) -> bool:
        
        valid = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        
        stack = []

        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if stack:
                    last = stack.pop()
                else:
                    return False
                
                if last == valid[i]:
                    continue
                else:
                    return False
        return False if stack else True
