from typing import List

class Solution1:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for customer in accounts:
            sum = 0
            for amount in customer:
                sum += amount
            if sum > result:
                result = sum
        return result

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        m = len(accounts)
        n = len(accounts[0])
        i = 0
        while i < m:
            sum = 0
            j = 0
            while j < n:
                sum += accounts[i][j]
                j += 1
            if sum > result:
                result = sum
            i += 1
        return result


def validateInput(accounts: List[List[int]]):
    m = len(accounts)
    assert 1 <= m and m <= 50
    for customer in accounts:
        n = len(customer)
        assert 1 <= n and n <= 50

        for amount in customer:
            assert 1 <= amount and amount <= 100
    return accounts


if __name__ == '__main__':
    sol = Solution()

    examples = [
        [[[1,2,3],[3,2,1]], 6],
        [[[1,5],[7,3],[3,5]], 10],
        [[[2,8,7],[7,1,3],[1,9,5]], 17]
    ]

    for example in examples:
        input, output = example
        assert output == sol.maximumWealth(validateInput(input))