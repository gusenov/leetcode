import string


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = True
        
        letters = {}
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            letters[letter] = 0

        for letter in magazine:
            letters[letter] += 1

        for letter in ransomNote:
            if letters[letter] > 0:
                letters[letter] -= 1
            else:
                result = False
                break

        return result


def validateInput(ransomNote: str, magazine: str):
    lowercaseEnglishLetters = string.ascii_lowercase

    assert 1 <= len(ransomNote) <= pow(10, 5)
    assert all(letter in lowercaseEnglishLetters for letter in ransomNote)

    assert 1 <= len(magazine) <= pow(10, 5)
    assert all(letter in lowercaseEnglishLetters for letter in magazine)


if __name__ == '__main__':

    examples = [
        [{'ransomNote': 'a', 'magazine': 'b'}, False],
        [{'ransomNote': 'aa', 'magazine': 'ab'}, False],
        [{'ransomNote': 'aa', 'magazine': 'aab'}, True]
    ]

    solution = Solution()
    for inputOutput in examples:
        input, output = inputOutput
        ransomNote, magazine = input['ransomNote'], input['magazine']
        validateInput(ransomNote, magazine)
        assert output == solution.canConstruct(ransomNote, magazine)
