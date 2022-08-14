class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            steps += 1
        return steps

if __name__ == '__main__':

    sol = Solution()

    examples = {
        14: 6,
        8: 4,
        123: 12
    }
    for input in examples:
        assert examples[input] == sol.numberOfSteps(input)
