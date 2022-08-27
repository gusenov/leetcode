from typing import List
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        :return: The majority element is the element that appears more than ⌊n / 2⌋ times. 
        """

        n = len(nums)
        majorityCnt = math.floor(n / 2)
        print("n = {}, ⌊n / 2⌋ = {}".format(n, majorityCnt))

        cnt = {}
        for i in nums:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
            if cnt[i] > majorityCnt:
                return i

        return None


def validateInput(nums: List[int]):
    n = len(nums)
    assert 1 <= n and n <= 5 * pow(10, 4)
    assert all(-pow(10, 9) <= i and i <= pow(10, 9) for i in nums)

    # You may assume that the majority element always exists in the array.

    return input


if __name__ == "__main__":

    examples = [
        [[3,2,3], 3],
        [[2,2,1,1,1,2,2], 2]
    ]

    sol = Solution()

    for input, expectedOutput in examples:
        actualOutput = sol.majorityElement(validateInput(input))
        print("Expected output = {}, actual output = {}".format(expectedOutput, actualOutput))
        assert expectedOutput == actualOutput
