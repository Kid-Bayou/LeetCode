class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def buildFinalString(inputStr):
            stack =[]
            for char in inputStr:
                if char != '#':
                    stack.append(char)
                elif stack:
                        stack.pop()
            return ''.join(stack)
                
        return buildFinalString(s) == buildFinalString(t)
