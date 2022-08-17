from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        if root:
            result += 1
            result += max(self.maxDepth(root.left), self.maxDepth(root.right))
        return result


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0


def checkConstraints(root: Optional[TreeNode]) -> int:
    sz = 0
    if root:
        sz += 1 + checkConstraints(root.left) + checkConstraints(root.right)
        assert -100 <= root.val <= 100
    return sz

if __name__ == '__main__':
    sol = Solution()

    examples = {
        TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))): 3,
        TreeNode(1, None, TreeNode(2)): 2
    }

    for i, input in enumerate(examples):
        print("Example {}:".format(i + 1))
        sz = checkConstraints(input)
        print("The number of nodes in the tree: {}".format(sz))
        assert 0 <= sz and sz <= pow(10, 4)
        output = sol.maxDepth(input)
        print("Binary tree's maximum depth: {}".format(output))
        assert examples[input] == output
