from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [None] * n

        fb = 'FizzBuzz'
        f = 'Fizz'
        b = 'Buzz'

        divisibleBy3 = False
        divisibleBy5 = False

        i = 1
        j = i - 1
        while i <= n:
            divisibleBy3 = i % 3 == 0
            divisibleBy5 = i % 5 == 0
            j = i - 1
            if divisibleBy3 and divisibleBy5:
                answer[j] = fb
            elif divisibleBy3:
                answer[j] = f
            elif divisibleBy5:
                answer[j] = b
            else:
                answer[j] = str(i)
            i += 1
        return answer