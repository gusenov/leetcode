from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        i = 1
        while fast:
            if i % 2 == 0:
                slow = slow.next
            fast = fast.next
            i += 1
        return slow


if __name__ == '__main__':
    solution = Solution()

    node3 = ListNode(3, ListNode(4, ListNode(5)))
    node4 = ListNode(4, ListNode(5, ListNode(6)))
    examples = {
        ListNode(1, ListNode(2, node3)): node3,
        ListNode(1, ListNode(2, ListNode(3, node4))): node4
    }

    for input in examples:
        output = solution.middleNode(input)
        assert output == examples[input]
