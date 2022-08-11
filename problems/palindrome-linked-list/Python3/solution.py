from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def lenOfList(self, head: Optional[ListNode]) -> int:
        n = head
        l = 0
        while n:
            l += 1
            n = n.next
        return l

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        result = True
        # NOTE: В некоторых функциях результат по умолчанию True, а в других False. Далее нужно опровергнуть результат по умолчанию.
        
        sz = self.lenOfList(head)

        n = head
        i = 0
        while n and i != int(sz / 2):  # получение центрального элемента.
            # print("i = {}".format(i))
            a  = n.val

            j = 0
            m = head
            while j < sz - i:  # итерирование до i-го элемента, если считать справа налево.
                b = m.val
                m = m.next
                j += 1

            # print("a = {}, b = {}".format(a, b))
            if a != b:
                result = False
                break

            n = n.next
            i += 1

        return result


def validateInput(Node):
    assert 0 <= Node.val and Node.val <= 9
    return Node


if __name__ == '__main__':

    examples = {
        ListNode(1, ListNode(2, ListNode(2, ListNode(1)))) : True,
        ListNode(1, ListNode(2)) : False,

        ListNode(1) : True,
        ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1))))) : True,
        ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))) : False
    }

    solution = Solution()
    for input in examples:
        print("result = {}".format(solution.isPalindrome(validateInput(input))))