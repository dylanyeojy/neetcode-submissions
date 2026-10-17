class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketDict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for index, bracket in enumerate(s):
            if len(stack) == 0:
                stack.append(bracket)
                continue
            
            stack.append(bracket)
            previousBracket = stack[len(stack) - 2]
            bracketLookUp = bracketDict.get(previousBracket)
            # print(stack)
            # print(f'Bracket: {bracket}')
            # print(f'Previous Bracket: {previousBracket}')
            # print(f'Bracket Look Up: {bracketLookUp}')
            # print()

            if bracket == bracketLookUp:
                stack.pop(-1)
                stack.pop(-1)
            else:
                continue
            
        if len(stack) == 0:
            return True
        else:
            return False