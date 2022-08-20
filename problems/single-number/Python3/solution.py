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

1.1) Зная, что искомый элемент нечетный рассмотрим все нечетные элементы чтобы найти среди них лишний:

(Н + Н) + (Н + Н) + Н

(7 + 7) + (5 + 5) + 3 = 27
   14   +    10   + 3 = 27
   Ч    +    Ч    + Н = Н

Наблюдение:
27 - 14 = 13 - простое
27 - 10 = 17 - простое
27 - 6  = 21

(3 + 3) + (5 + 5) + 7 = 23
   6    +    10   + 7 = 23
   Ч    +    Ч    + Н = Н

Наблюдение:
23 - 6  = 17 - простое
23 - 10 = 13 - простое
23 - 7  = 16

Предположение: если разность суммы нечетных элементов и 2*twice[i] не простое число, то это искомый элемент.

(1 + 1) + (3 + 3) + (-1) = 7
   2    +    6    + (-1) = 7
7 - 2 = 5 - простое
7 - 6 = 1 - не простое (!)
7 - (-1) = 8 - не простое

1.2)

(Ч + Ч) + (Ч + Ч) + Н

(2 + 2) + (4 + 4) + 9 = 21
   4    +    8    + 9 = 21
21 - 4  = 17
21 - 8  = 13
21 - 18 = 3
Здесь мы рассматривали все элементы, хотя известно, что сумма нечетная.
Что если рассматривать только нечетные элементы?

2) (Ч + Ч) + (Н + Н) + Ч = Ч;

(Ч + Ч) + (Ч + Ч) + Ч

(2 + 2) + (4 + 4) + 6 = 18
   4    +    8    + 6 = 18

С четными можно поступать также как с нечетными просто добавляя +1.
Возможно потому что Ч + Ч = Ч, а Ч + Н = Н.
'''


class Solution:
    def is_prime(self, n):
        # Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1. 
        # Именно этим оно отличается от всех остальных натуральных чисел. 
        # Число 2 — первое наименьшее простое, единственное четное, простое число.
        if 1 == n:
            return False
        
        for i in range(2, n):
            if 0 == n % i:
                return False
        return True

    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        l = len(nums)
        
        sum = 0
        i = 0
        while i < l:
            sum += nums[i]
            i += 1

        r = sum % 2
        print("Σ = {}. Is Σ odd? {}".format(sum, r))

        j = 0 if r else 1

        odd_sum, odd_cnt = 0, 0

        base = 3 * pow(10, 4)

        i = 0
        while i < l:
            if r == nums[i] % 2:
                odd_sum += nums[i] + (j if nums[i] > 0 else -j)
                odd_cnt += 1
            i += 1

        print("Odd sum = {}, cnt = {}".format(odd_sum, odd_cnt))
        if 1 == odd_cnt:
            result = odd_sum if r else odd_sum - (j if odd_sum > 0 else -j)
        else:
            i = 0
            while i < l:
                if r == nums[i] % 2:
                    n = nums[i] + (j if nums[i] > 0 else -j)
                    if not self.is_prime(odd_sum - (2 * n)):
                        result = nums[i]
                        break
                i += 1
        
        return result


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
        [ [-1, -1, -2], -2 ]
    ]
    examples = [
        [ [2,2,1], 1 ],
        [ [4,1,2,1,2], 4 ],
        [ [1], 1 ],

        [ [2,2,4,4,6], 6 ],
        [ [2,2,4,4,1], 1],
        [ [2,2,4,4,9], 9],
        [ [5,3,7,5,7], 3 ],
        [ [3,3,5,5,7], 7 ],
        [ [5,3,3], 5 ],
        [ [1,1,2], 2 ],

        [ [-1,-1,-2], -2 ],
        [ [1,3,1,-1,3], -1 ]
    ]



    for input, excpectedOutput in examples:
        print("Input: {}".format(input))
        actualOutput = sol.singleNumber(validate(input))
        print("Output: {}".format(actualOutput))
        assert excpectedOutput == actualOutput
        print()
