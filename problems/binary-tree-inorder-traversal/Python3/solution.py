from doctest import Example
import enum
from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            if root.left:
                result += self.inorderTraversal(root.left)
            result.append(root.val)
            if root.right:
                result += self.inorderTraversal(root.right)
        return result


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        s = []
        
        node = root
        r = False

        while node:
            if node.left and not r:
                s.append(node)
                node = node.left
                r = False
            else:
                result.append(node.val)
                if node.right:
                    # Здесь не помещаем в стек потому что обработка этого узла закончена.
                    node = node.right
                    r = False
                else:
                    node = s.pop() if s else None
                    r = True
        return result


def validate(root: Optional[TreeNode]):
    numberOfNodes = 0
    if root:
        numberOfNodes += 1
        return numberOfNodes + validate(root.left) + validate(root.right)
    return numberOfNodes


if __name__ == '__main__':
    sol = Solution()
    examples = {
        TreeNode(1, None, TreeNode(2, TreeNode(3), None)): [1, 3, 2],
        None: [],
        TreeNode(1, None, None): [1],

        TreeNode('F', TreeNode('B', TreeNode('A'), TreeNode('D', TreeNode('C'), TreeNode('E'))), TreeNode('G', None, TreeNode('I', TreeNode('H'), None))): ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    }
    for input in examples:
        numberOfNodes = validate(input)
        print("The number of nodes in the tree: {}".format(numberOfNodes))
        assert 0 <= numberOfNodes <= 100
        output = sol.inorderTraversal(input)
        print("Output: {}".format(output))
        assert examples[input] == output
