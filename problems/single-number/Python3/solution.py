from doctest import Example
from typing import List


# You must implement a solution with a linear runtime complexity and use only constant extra space.


'''
Н + Н = Ч
Ч + Ч = Ч
Ч + Н = Н

Σ 2*twice[i] всегда четная. Т.к.
1) Сумма двух одинаковых чисел всегда четная: (Ч + Ч) + (Н + Н) = Ч + Ч.
2) Сумма всех четных сумм тоже будет четной: Ч + Ч + Ч = (Ч + Ч) + Ч = Ч + Ч.

Если  Σ 2*twice[i] + one  четная, то one четное (Ч + Ч = Ч), иначе нечетное (Ч + Н = Н):

1) (Ч + Ч) + (Н + Н) + Н = Н.

    1.1)

        (Н + Н) + (Н + Н) + Н = Н
           Ч    +    Ч    + Н = Н

        (7 + 7) + (5 + 5) + 3 = 27
           14   +    10   + 3 = 27

        (3 + 3) + (5 + 5) + 7 = 23
           6    +    10   + 7 = 23

        (1 + 1) + (3 + 3) + 5 = 13
           2    +    6    + 5 = 13

        (1 + 1) + (3 + 3) + 30001 = 30009
           2    +    6    + 30001 = 30009

        (1 + 1) + (3 + 3) + (-1) = 7
           2    +    6    + (-1) = 7

    1.2)

        (Ч + Ч) + (Ч + Ч) + Н = Н
           Ч    +    Ч    + Н = Н

        (2 + 2) + (4 + 4) + 9 = 21
           4    +    8    + 9 = 21

2) (Ч + Ч) + (Н + Н) + Ч = Ч;

    (Ч + Ч) + (Ч + Ч) + Ч = Ч
       Ч    +    Ч    + Ч = Ч

    (2 + 2) + (4 + 4) + 6 = 18
       4    +    8    + 6 = 18

С четными можно поступать также как с нечетными просто добавляя +1.
Возможно потому что Ч + Ч = Ч, а Ч + Н = Н.
'''


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        l = len(nums)
        
        sum = 0
        i = 0
        while i < l:
            sum += nums[i]
            i += 1
        r = sum % 2
        print("Σ = {}. Is Σ odd? {}".format(sum, r))

        d = {}

        i = 0
        while i < l:
            if r == nums[i] % 2:
                if nums[i] in d:
                    d[nums[i]] += 1
                else:
                    d[nums[i]] = 1
            i += 1
        
        for n in d:
            if 1 == d[n]:
                print("Result: {}".format(n))
                return n

        print("Failed: {}".format(d))
        assert False


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        for n in d:
            if 1 == d[n]:
                return n


def validate(nums: List[int]):
    assert 1 <= len(nums) and len(nums) <= (3 * pow(10, 4))
    assert all((-3 * pow(10, 4)) <= n <= (3 * pow(10, 4)) for n in nums)


    # Each element in the array appears twice except for one element which appears only once.

    appears_cnt = {}
    for n in nums:
        if n in appears_cnt:
            appears_cnt[n] += 1
        else:
            appears_cnt[n] = 1
    
    one_cnt = 0
    for k, v in appears_cnt.items():
        assert 1 == v or 2 == v
        if 1 == v:
            one_cnt += 1
    assert 1 == one_cnt


    return nums


if __name__ == "__main__":
    sol = Solution()

    examples = [
        [ [2,2,1], 1 ],
        [ [4,1,2,1,2], 4 ],
        [ [1], 1 ],

        [ [1,1,2], 2 ],
        [ [1,2,2], 1 ],
        [ [2,2,4,4,6], 6 ],
        [ [2,2,4,4,1], 1],
        [ [2,2,4,4,9], 9],
        [ [5,3,7,5,7], 3 ],
        [ [3,3,5,5,7], 7 ],
        [ [5,3,3], 5 ],
        [ [1,1,2], 2 ],
        [ [1,3,1,5,3], 5 ],
        # [ [1,3,1,30001,3], 30001 ],

        [ [-1,-1,-2], -2 ],
        [ [1,3,1,-1,3], -1 ]
    ]

    # examples = [  [ [1,3,1,30001,3], 30001 ]  ]

    for input, excpectedOutput in examples:
        print("Input: {}".format(input))
        
        
        actualOutput = sol.singleNumber(validate(input))
        # actualOutput = sol.singleNumber(input)

        print("Output: {}".format(actualOutput))
        assert excpectedOutput == actualOutput
        print()
