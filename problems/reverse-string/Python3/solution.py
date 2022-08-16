from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def validate(s: List[str]):
    assert 1 <= len(s) and len(s) <= pow(10, 5)
    assert is_ascii(s)


if __name__ == '__main__':
    sol = Solution()

    examples = [
        [["h","e","l","l","o"], ["o","l","l","e","h"]],
        [["H","a","n","n","a","h"], ["h","a","n","n","a","H"]]
    ]

    for input, output in examples:
        validate(input)
        sol.reverseString(input)
        assert output == input
