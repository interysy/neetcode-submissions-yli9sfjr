class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = [] 
        operators = {"+","-","*","/"}
         

        for index, token in enumerate(tokens): 
            if token.lstrip('-').isdigit():
                stack.append(token) 
            elif token in operators:
                secondary = stack.pop()
                primary = stack.pop() 

                expression_string = f"{primary}{token}{secondary}"
                result = int(eval(expression_string))

               
                stack.append(result) 

        return int(stack[-1])


        