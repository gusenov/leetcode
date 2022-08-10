# Roman numerals are represented by seven different symbols:
ROMAN_SYMBOLS = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

SYMBOL_TO_VALUE = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,

    # I can be placed before V (5) and X (10) to make 4 and 9.
    'IV' : 4,
    'IX': 9,
    
    # X can be placed before L (50) and C (100) to make 40 and 90. 
    'XL': 40,
    'XC': 90,

    # C can be placed before D (500) and M (1000) to make 400 and 900.
    'CD': 400,
    'CM': 900
}

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        result = 0
        window = ''
        for symbol in s:
            window += symbol

            if len(window) == 3:
                first_two_char = window[:2]
                if first_two_char in SYMBOL_TO_VALUE:
                    result += SYMBOL_TO_VALUE[first_two_char]
                    window = window[2:]
                else:
                    result += SYMBOL_TO_VALUE[window[0]]
                    window = window[1:]
                
        if window:
            if window in SYMBOL_TO_VALUE:
                result += SYMBOL_TO_VALUE[window]
            else:
                for symbol in window:
                    result += SYMBOL_TO_VALUE[symbol]

        return result


def validateInput(s):
    assert 1 <= len(s) and len(s) <= 15
    assert all(symbol in ROMAN_SYMBOLS for symbol in s)
    return s


def validateOutput(output):
    assert 1 <= output and output <= 3999
    return output


if __name__ == '__main__':
    solution = Solution()
    examples = {
        'III': 3,
        'LVIII': 58,
        'MCMXCIV': 1994
    }
    for input in examples:
        assert examples[input] == validateOutput(solution.romanToInt(validateInput(input)))
