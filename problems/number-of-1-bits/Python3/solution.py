from traceback import print_tb


class Solution:
    def hammingWeight(self, n: int) -> int:

        if n >= 0:
            
            numberOfOneBits = 0
            
            while n != 0:
                if n & 1:
                    numberOfOneBits += 1
                n = n >> 1
        
        else:

            numberOfOneBits = 32

            while n != -1:
                if not (n & 1):
                    numberOfOneBits -= 1
                n = n >> 1

        return numberOfOneBits


def testShift(x):
    print("x = {} = {}".format(x, bin(x)))
    
    for y in range(1, 3):
        print("x << {} = {} = {}".format(y, x << y, bin(x << y)))
    
    for y in range(1, 3):
        print("x >> {} = {} = {}".format(y, x >> y, bin(x >> y)))


def testAnd(x):
    print("Binary representation of {}: {}".format(x, bin(x)))
    s = []
    while x:
        if x & 1:
            s.insert(0, 1)
        else:
            s.insert(0, 0)
        x = x >> 1
    print(s)


if __name__ == "__main__":

    sol = Solution()

    examples = [
        ['00000000000000000000000000001011', 11, 3],
        ['00000000000000000000000010000000', 128, 1],
        ['11111111111111111111111111111101', -3, 31]
    ]

    for inputBinStr, inputDec, expectedOutput in examples:       
        print("Input: n = {}".format(inputBinStr))
        inputBin = int(inputBinStr, 2)
        print("Converted binary string to int: {}".format(inputBin))
        print("Binary representation of {}: {}".format(inputDec, bin(inputDec)))

        print("Expected output: {}".format(expectedOutput))
        actualOutput = sol.hammingWeight(inputDec)
        print("Actual output: {}".format(actualOutput))

        assert expectedOutput == actualOutput

        print()
