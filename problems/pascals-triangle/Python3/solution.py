from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Pascal's Triangle

        :param numRows: 
        :return: the first numRows of Pascal's triangle.
        """
        result = [[1]]
        for numRow in range(1, numRows):
            row = [1]
            for i in range(1, len(result[numRow - 1])):
                # In Pascal's triangle, each number is the sum of the two numbers directly above it
                row.append(result[numRow - 1][i - 1] + result[numRow - 1][i])
            row.append(1)
            result.append(row)
        return result


def validate(numRows):
    assert 1 <= numRows and numRows <= 30
    return numRows


if __name__ == "__main__":

    examples = {
        1: [[1]],
        5: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    }

    sol = Solution()
    for input, expectedOutput in examples.items():
        actualOutput = sol.generate(validate(input))
        assert expectedOutput == actualOutput
