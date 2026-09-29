class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # length of 0 -> return 0
        # length of 1 -> return 1 
        # length of 2 -> check if different, if so 2, otherwise 1
        # all repeating characters -> algo should work 


        length_s = len(s) 
        # print(f"length {length_s}")

        if length_s == 0 or length_s == 1: 
            return length_s 

        if length_s == 2: 
            return (1 if s[0] == s[1] else 2)


        front = 0
        back = 1
        seen = set(s[0])
        maximum_length = 1
        current_length = 1

        while back < length_s: 
            if front == back: 
                current_length += 1
                seen.add(s[front])
                back += 1
                continue

            # print(back)
            considering = s[back]

            # print(f"considering {s[front:back]}")
            # print(f"to add {considering}")
            # print(f"current length {current_length}")
            # print(seen)

            if considering in seen: 
                seen.discard(s[front])
                front += 1
                current_length -= 1
                # print("seen")
            else: 
                back += 1
                current_length += 1
                seen.add(considering)
                # print("not seen")


            if current_length > maximum_length: 
                maximum_length = current_length



        return maximum_length
        