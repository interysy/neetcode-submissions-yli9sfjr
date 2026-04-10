class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        # use a monotonic stack

        stack = [] 
        results = [0] * len(temperatures)


        for temperature_index,temperature in enumerate(temperatures): 

            # print(f"Current index {temperature_index}")
            # print(f"Current temperature {temperature}")

            if len(stack) == 0: 
                # print("case 1")
                stack.append((temperature_index, temperature)) 
                # print(stack)
                continue 

            top_temperature = stack[-1] 

            if temperature > top_temperature[1]: 
                # print("case 2")
                # iterate through stack and fill
                stack_element = stack[-1]
                while len(stack) != 0 and stack_element[1] < temperature: 
                    stack.pop()
                    results[stack_element[0]] = temperature_index - stack_element[0]

                    if len(stack) != 0:
                        stack_element = stack[-1] 
                
                stack.append((temperature_index, temperature))
                # print(stack)
                # print(results)
            else: 
                # print("case 3")
                stack.append((temperature_index, temperature))
                # print(stack)
            

        # print(results)
        return results

        