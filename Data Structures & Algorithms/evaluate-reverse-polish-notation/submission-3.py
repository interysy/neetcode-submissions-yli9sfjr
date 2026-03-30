class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = [] 
        operators = {"+","-","*","/"}
         

        for index, token in enumerate(tokens): 
            if token.lstrip('-').isdigit():
                print(f"appending {token}")
                stack.append(token) 
            elif token in operators:
                secondary = stack.pop()
                primary = stack.pop() 

                expression_string = f"{primary}{token}{secondary}"

                print(f"expression string {expression_string}")

                result = int(eval(expression_string))

                if index == len(tokens)-1:
                    return result
                else: 
                    stack.append(result) 

            print(stack)

        return int(stack[-1])


        