import string


# Time Limit Exceeded	
# Executed input: https://leetcode.com/submissions/detail/784530823/testcase/
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:

        sz = len(t)
        if sz != len(s):
            return False
        
        free = [True] * sz

        i, j = 0, 0
        while i < sz:
            j = 0
            while j < sz:
                if free[j] and s[i] == t[j]:
                    free[j] = False
                    break
                j += 1
            if j == sz:
                return False
            i += 1

        return True


class Solution:
    def countLetters(self, word: str):
        result = {}
        for letter in string.ascii_lowercase:
            result[letter] = 0
        for letter in word:
            result[letter] += 1
        return result

    def isAnagram(self, s: str, t: str) -> bool:
        wordLettersCnt = self.countLetters(s)
        anagramLettersCnt = self.countLetters(t)
        return wordLettersCnt == anagramLettersCnt
        

def validateInput(s: str, t: str):
    for stri in [s, t]:
        assert 1 <= len(stri) and len(stri) <= 5 * pow(10, 4)
        assert all(letter in string.ascii_lowercase for letter in stri)


if __name__ == "__main__":

    examples = [
        [["anagram", "nagaram"], True],
        [["rat", "car"], False],
        
        [["a", "ab"], False]
    ]

    sol = Solution()
    for input, expectedOutput in examples:
        s, t = input
        print("Input: s = {}, t = {}".format(s, t))
        print("Expected output: {}".format(expectedOutput))
        validateInput(s, t)
        actualOutput = sol.isAnagram(s, t)
        assert expectedOutput == actualOutput
        print()
