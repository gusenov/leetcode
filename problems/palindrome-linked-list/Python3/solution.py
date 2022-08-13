from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
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


class Solution2:
    def prt(self, head: Optional[ListNode]):
        n = head
        while n:
            print(n.val, end=' ')
            n = n.next
        print()

    def eq(self, i, j):
        result = True

        if (i and not j) or (not i and j):
            return False
        
        while True:

            if i.val != j.val:
                result = False
                break

            i = i.next
            j = j.next

            if not i and not j:
                break
            
            if (i and not j) or (not i and j):
                result = False
                break
        
        return result

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = head
        m = None
        sz = 0
        result = {}
        while n:
            sz += 1
            m0 = m
            m = n
            n = n.next
            m.next = m0

            #self.prt(m)
            if n and m:
                e1, e2 = self.eq(n, m), self.eq(n.next, m)
                result[sz] = [e1, e2]
                #print(e1, e2)

            result.pop(int(sz / 2) - 1, None)
        
        c = int(sz / 2)
        if sz == 1:
            return True
        elif sz % 2 == 0:
            return result[c][0]
        else:
            return result[c][1]
        

class Solution:
    def length(self, head: Optional[ListNode]) -> int:
        result = 0
        node = head
        while node:
            result += 1
            node = node.next
        return result

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = True

        size = self.length(head)

        start = int(size / 2)
        if size % 2:
            start += 1

        s = []

        node = head
        i = 0
        while i != start:
            s.append(node.val)
            node = node.next
            i += 1
        
        if size % 2:
            s.pop()

        while node:
            if node.val != s.pop():
                result = False
                break
            node = node.next
        
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
        output = solution.isPalindrome(validateInput(input))
        assert examples[input] == output
