from email import header
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        if self.next and other.next:
            return ((self.val, self.next) == (other.val, other.next))
        elif self.next or other.next:
            return False
        else:
            return ((self.val) == (other.val))

    def __str__(self):
        result = ''
        node = self
        while node:
            result += str(node.val)
            if (node.next):
                result += ', '
            node = node.next
        return result

    def __len__(self):
        result = 0
        n = self
        while n is not None:  # Если написать просто while n: то будет бесконечная рекурсия потому что при проверке узла вызывается этот же метод.
            result += 1
            n = n.next
        return result


# iteratively
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head
        p = None
        while n:
            m = n.next  # запоминаем сразу следующий у текущего.
            n.next = p  # меняем следующий у следующего на предыдущий.
            p = n       # запоминаем текущий как предыдущий.
            n = m       # переходим к исходному следующему.
        return p


# recursively
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            if head.next is None:
                return head
            else:
                tail = self.reverseList(head.next)  # сразу получим последний узел, который будет результатом.
                head.next.next = head               # меняем следующий у следующего на текущий.
                head.next = None                    # обнуляем следующий у текущего, позже он перезапишется, если возможно будет.
                return tail


def validateInput(head: Optional[ListNode]) -> Optional[ListNode]:
    if head:

        sz = len(head)
        assert 0 <= sz and sz <= 5000

        n = head
        while n:
            assert -5000 <= n.val <= 5000
            n = n.next
    
    return head


if __name__ == '__main__':
    sol = Solution()

    examples = {
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))): ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))),
        ListNode(1, ListNode(2)): ListNode(2, ListNode(1)),
        None: None
    }

    for input in examples:
        actualOutput = sol.reverseList(validateInput(input))
        if input:
            print(actualOutput)
            assert examples[input] == actualOutput
        else:
            assert not actualOutput
