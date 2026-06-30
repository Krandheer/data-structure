# linked list palindrome


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    stack = []
    node = head
    lent = 0
    while node:
        lent += 1
        node = node.next
    node = head
    temp = 0
    while node:
        if temp >= lent // 2:
            if stack and node.val == stack[-1]:
                stack.pop()
        else:
            stack.append(node.val)
        temp += 1
        node = node.next

    if not stack:
        return True

    return False


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print(isPalindrome(head))
