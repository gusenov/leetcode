from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        soldiersByRow = []
        for i, row in enumerate(mat):
            soldiers = 0
            for val in row:
                if val == 1:
                    soldiers += 1
                else:
                    break
            soldiersByRow.append([i, soldiers])
        soldiersByRow.sort(key=lambda x: (x[1], x[0]))
        result = [int(item[0]) for item in soldiersByRow[:k]]
        return result


def validateInput(mat: List[List[int]], k: int):
    m = len(mat)
    assert m <= 100
    assert 1 <= k and k <= m
    for i, row in enumerate(mat):
        n = len(row)
        assert 2 <= n
        for j, val in enumerate(row):
            assert val == 0 or val == 1


if __name__ == '__main__':
    sol = Solution()
    examples = [
        [
            [[1,1,0,0,0],
             [1,1,1,1,0],
             [1,0,0,0,0],
             [1,1,0,0,0],
             [1,1,1,1,1]],
            3,
            [2,0,3]  # Output
            # Explanation: 
            # The number of soldiers in each row is: 
            # - Row 0: 2 
            # - Row 1: 4 
            # - Row 2: 1 
            # - Row 3: 2 
            # - Row 4: 5 
            # The rows ordered from weakest to strongest are [2,0,3,1,4].
        ],
        [
            [[1,0,0,0],
             [1,1,1,1],
             [1,0,0,0],
             [1,0,0,0]], 
            2,
            [0,2]  # Output
            # Explanation: 
            # The number of soldiers in each row is: 
            # - Row 0: 1 
            # - Row 1: 4 
            # - Row 2: 1 
            # - Row 3: 1 
            # The rows ordered from weakest to strongest are [0,2,3,1].
        ]
    ]

    for example in examples:
        mat, k, output = example
        validateInput(mat, k)
        assert output == sol.kWeakestRows(mat, k)
