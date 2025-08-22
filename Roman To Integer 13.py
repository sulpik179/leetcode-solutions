class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, 
             "V": 5, 
             "X": 10, 
             "L": 50, 
             "C": 100, 
             "D": 500, 
             "M": 1000}

        char_list = list(s)
        total = 0
        p_value = 0
        for char in reversed(char_list):
            c_value = roman[char]
            if c_value < p_value:
                total -= c_value
            else:
                total += c_value
            p_value = c_value
        return total

       
