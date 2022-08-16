# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def numberOfNodes(self):
        result = 0
        n = self
        while n:
            result += 1
            n = n.next
        return result

    def valueOfEachNodeInListIsUnique(self):
        values = []
        sz = 0
        n = self
        while n:
            values.append(n.val)
            sz += 1
            n = n.next
        return sz == len(set(values))

    def tailNode(self):
        result = None
        n = self
        while n:
            result = n
            n = n.next
        return result

    def toString(self):
        result = ''
        n = self
        while n:
            result += "{}".format(n.val)
            n = n.next
            if n:
                result += ', '
        return result


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        n = node
        while n.val != node.val:
            n = n.next
        while n:
            m = n.next
            n.val = m.val
            if m.next:
                n = m
            else:
                n.next = None
                break
            


def validate(head, node):
    num = head.numberOfNodes()
    assert 2 <= num and num <= 1000

    n = head
    while n:
        assert -1000 <= n.val and n.val <= 1000
        n = n.next

    assert head.valueOfEachNodeInListIsUnique()
    assert head.tailNode() != node


if __name__ == '__main__':
    sol = Solution()

    node5 = ListNode(5, ListNode(1, ListNode(9, None)))
    head1 = ListNode(4, node5)

    node1 = ListNode(1, ListNode(9, None))
    head2 = ListNode(4, ListNode(5, node1))

    node2 = ListNode(2, ListNode(0, ListNode(1, ListNode(3))))
    head3 = node2

    examples = [
        [head1, node5, '4, 1, 9'],
        [head2, node1, '4, 5, 9'],
        [head3, node2, '0, 1, 3']
    ]

    for head, node, output in examples:
        validate(head, node)
        sol.deleteNode(node)
        assert output == head.toString()