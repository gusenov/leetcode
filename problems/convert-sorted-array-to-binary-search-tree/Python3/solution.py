from typing import List, Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        """
        Печать дерева по уровням сверху вниз. Сначала первая строка, потом вторая и т.д.
        """

        result = ''

        q = [self]
        while q:
            n = q.pop(0)  # извлекаем первый узел в очереди.
            if n:
                if result:
                    result += ","
                result += str(n.val)  # добавляем к строке значение очередного узла.
                q.append(n.left)  # помещаем в очередь первый дочерний узел.
                q.append(n.right)  # помещаем в очередь второй дочерний узел.
            else:
                if all(not m for m in q):  # если в очереди остались только нулевые узлы, то прекращаем вывод.
                    break
                if result:
                    result += ","
                result += "null"
        
        return "[{}]".format(result)


"""
# 1

  0   1  2  3  4
  1   2  3  4  5
-10  -3  0  5  9
         A

  0   1  A  0  1
-10  -3     5  9

# 2

 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
                      A

 0  1  2  3  4  5  6  A  0  1  2  3  4  5  6
 1  2  3  4  5  6  7     9 10 11 12 13 14 15
          B                       B

 0  1  2  B  0  1  2  A  0  1  2  B  0  1  2
 1  2  3     5  6  7     9 10 11    13 14 15
    C           C           C           C 

 0     0  B  0     0  A  0     0  B  0     0
 1     3     5     7     9    11    13    15
    C           C           C           C 
 D     D     D     D     D     D     D     D
"""

class Solution:
    """
    Суть решения в том чтобы делить строго отсортированный массив пополам и из центрального элемента создавать новый узел.
    Из-за деления пополам левое и правое поддеревья будут равны по размеру (+/- 1).
    В бинарном дереве поиска значение из левого подузла меньше значения в текущем узле
    и значение из правого подузла больше значения в текущем узле.
    """

    def divide(self, nums: List[int], parentNode: Optional[TreeNode], first: int, sz: int):
        # Делим список пополам.
        betterHalf = math.ceil(sz / 2)  # бОльшая половина.
        
        # Конечный элемент первой бОльшей половины будем считать серединой.
        middleIndex = first + betterHalf - 1  # индекс центрального элемента.
        middleValue = nums[middleIndex]

        leftSz = betterHalf - 1  # -1 потому что забираем один элемент для нового узла.
        rightSz = sz - betterHalf

        newNode = TreeNode(middleValue)
        if parentNode:
            if middleValue < parentNode.val:
                parentNode.left = newNode
            else:
                parentNode.right = newNode

        print("first: {}, sz: {}, midIdx: {}, midVal: {}, lsz: {}, rsz: {}".format(first, sz, middleIndex, middleValue, leftSz, rightSz))

        if leftSz:
            self.divide(nums, newNode, first, leftSz)

        if rightSz:
            self.divide(nums, newNode, middleIndex + 1, rightSz)

        return newNode

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Convert Sorted Array to a height-balanced Binary Search Tree

        :param nums: an integer array nums where the elements are sorted in ascending order
        :return: A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
        """
        
        return self.divide(nums, None, 0, len(nums))



def validate(nums: List[int]):
    assert 1 <= len(nums) and len(nums) <= pow(10, 4)  # 1 <= nums.length <= 10^4
    p = None
    for i in nums:
        assert -pow(10, 4) <= i and i <= pow(10, 4)  # -10^4 <= nums[i] <= 10^4
        if p:
            assert i > p  # nums is sorted in a strictly increasing order.
        p = i
    return nums


if __name__ == "__main__":
    examples = [
        # Input: nums = [-10,-3,0,5,9]
        [ [-10,-3,0,5,9], [
            
            #          0    
            #    -3         9
            # -10          5
            TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5))),

            #        0    
            # -10         5
            #    -3        9
            TreeNode(0, TreeNode(-10, None, TreeNode(-3)), TreeNode(5, None, TreeNode(9)))
        ] ],
        # [0,-10,5,null,-3,null,9] is also accepted:
        
        # Input: nums = [1,3]
        # [1,null,3] and [3,1] are both height-balanced BSTs.
        [ [1,3], [
            
            #  3
            # 1
            TreeNode(3, TreeNode(1)),
            
            # 1
            #  3
            TreeNode(1, None, TreeNode(3))
        ] ],

        [ [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [
            TreeNode(8, TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), TreeNode(12, TreeNode(10, TreeNode(9), TreeNode(11)), TreeNode(14, TreeNode(13), TreeNode(15))))
        ] ],

        #                       10
        #          3                         16
        #   2           4              13          17
        #                                                18
        [ [2,3,4,10,13,16,17,18], [
            TreeNode(10, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(16, TreeNode(13), TreeNode(17, None, TreeNode(18))))
        ] ]
    ]

    sol = Solution()

    for input, acceptedOutputs in examples:
        print("Input: {}".format(input))
        for expectedOutput in acceptedOutputs:
            print("Expected output: {}".format(expectedOutput))
        
        actualOutput = sol.sortedArrayToBST(validate(input))
        print("Actual output: {}".format(actualOutput))
        print()
    