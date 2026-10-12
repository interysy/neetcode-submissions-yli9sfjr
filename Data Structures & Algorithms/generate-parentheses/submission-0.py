class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(opened = 0, closed = 0):
            if opened == closed == n: 
                res.append("".join(stack))
                return 
            
            if opened < n: 
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()

            if closed < opened: 
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()

        backtrack()
        return res


        

        


        