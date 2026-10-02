from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        length_s = len(s)

        if length_s == 1:
            return 1

        if length_s == 2:
            if k > 1 or s[0] == s[1]: 
                return 2
            else: 
                return 1


        seen = defaultdict(int)
        seen[s[0]] = 1
        most_frequent = s[0]
        max_length = 1
        current_length = 1

        left = 0

        for right in range(1, length_s):
            # print(f"current {s[right]}")
            if s[right] == most_frequent: 
                # print(f"equal to most frequent {s[right]}")
                current_length += 1
                seen[most_frequent] += 1
            else: 
                # print("unequal")
                if seen.get(s[right], None) == None: 
                    seen[s[right]] = 1
                else:
                    seen[s[right]] += 1

                most_frequent = max(seen, key=seen.get)


                # print("enter loop to find correct k")
                while ((right - left + 1) - seen[most_frequent]) > k: 
                    # print(f"shortened to {s[left : right + 1]}")
                    seen[s[left]] -= 1
                    left += 1
                    #O(26)
                    # print(seen)
                    most_frequent = max(seen, key=seen.get)
                    # print(f"most frequent {most_frequent}")

                temp_k = ((right - left + 1) - seen[most_frequent])
                # print(f"k {temp_k}")
                current_length = (right - left + 1)


            max_length = max(max_length, current_length) 

        return max_length

