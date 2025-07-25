class Solution:
    def intToRoman(self, num: int) -> str:
        num_list = list(map(int, str(num)))
        res_list = []
        num_len = len(num_list)
        for value in num_list:
            res_list.append(MyMethod.diff(value, num_len))
            num_len -= 1
        result = "".join(res_list)
        return result
class MyMethod:
    def diff(value, num_len):
        n = 10**(num_len - 1)
        roman = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        if num_len == 4:
            return roman[1000] * value
        else:
            while True:
                if value == 9:
                    return roman[10**(num_len - 1)] + roman[10**num_len]
                elif value == 4:
                    return roman[n] + roman[5 * n]
                elif value < 4:
                    return roman[n] * value
                else:
                    di = value - 5
                    return roman[5 * n] + roman[1 * n] * di