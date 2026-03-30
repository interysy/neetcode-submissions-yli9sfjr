class Solution:
    def isPalindrome(self, s: str) -> bool:


        s = s.lower()
        start = 0 
        end = len(s) - 1

        while start < end: 
            start_element = s[start] 
            end_element = s[end] 

            # print(f"start {start_element}")
            # print(f"end {end_element}")

            # print("here")

            if (not start_element.isalnum()):
                # print("start not a num")
                start += 1 
                continue
            if (not end_element.isalnum()):
                # print("end not a num")
                end -=1 
                continue

            # print("here2")

            if start_element != end_element: 
                # print("NOT EQUAL")
                return False 

            # print("lol")

            start +=1 
            end -= 1
        return True

        