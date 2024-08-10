class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { ')' : '(' , '}' : '{' , ']' : '[' }
        stack = []

        for char in s:
            if char in brackets:
                topElement = stack.pop() if stack else '#'

                if brackets[char] != topElement:
                    return False
            else:
                stack.append(char)
        return not stack
