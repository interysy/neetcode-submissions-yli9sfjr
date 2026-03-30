class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] 
        pairs = {')' :'(','}' : '{',']': '['}
        brackets = ['(',  '{', '[']

        index = 0 
        while index != len(s): 
            character = s[index]

            if character in brackets: 
                stack.append(character)
            elif character in pairs: 
                if len(stack) > 0 and pairs[character] == stack[-1]: 
                    stack.pop()
                else: 
                    return False

            index += 1 

        return True if len(stack) == 0 else False