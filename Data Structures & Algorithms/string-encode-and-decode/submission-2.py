class Solution:

    SPLITTER = "℠"

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0: 
            return ""

        prefix = ""
        final_string = ""

        for index, string in enumerate(strs):
            print(string)
            if index == 0: 
                print("index 0 case")
                prefix +=  str(len(string))
                final_string += string
            else: 
                print("standard case")
                prefix += self.SPLITTER + str(len(string))
                final_string += string

            print(final_string)
            print(prefix)

        prefix += self.SPLITTER

        print(f"PREFIX {prefix}")


        print(prefix+final_string)
        return prefix + final_string 
            


    def decode(self, s: str) -> List[str]:

        if len(s) == 0: 
            return []
    
        start_position = 0
        end_position  = s.rindex(self.SPLITTER)
        print(end_position)

        lengths = []
        number = ""
        index = 0
        while index <= end_position: 
            print(f"character {s[index]}")
            if s[index] == self.SPLITTER: 
                # print("breaker")
                lengths.append(int(number))
                number = ""
            else: 
                number += s[index]
            index += 1

        print(lengths) 
        s = s[end_position+1:]

        index = 0
        strs = []
        for length in lengths: 
            strs.append(s[index: index+length])
            index = index + length 





        return strs
        # while amount != 0: 
            


