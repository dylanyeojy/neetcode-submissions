class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketDict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for bracket in s:
            if len(stack) == 0:
                stack.append(bracket)
                continue
            
            stack.append(bracket)
            previousBracket = stack[len(stack) - 2]
            bracketLookUp = bracketDict.get(previousBracket)
            # print(stack)
            # print(f'Bracket: {bracket}')
            # print(f'Previous Bracket: {previousBracket}')
            # print(f'Bracket Look Up: {bracketLookUp}\n')

            if bracket == bracketLookUp:
                stack.pop()
                stack.pop()
        
        return len(stack) == 0

