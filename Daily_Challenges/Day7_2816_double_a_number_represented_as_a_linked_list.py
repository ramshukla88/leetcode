# Date: 07-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        current = head
        before = None
        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after
        head = before
        current = head
        carry = 0
        while current is not None:
            temp = current.val * 2 + carry
            carry = int(temp/10)
            current.val = temp%10
            if current.next is None and carry == 1:
                new_node = ListNode(carry)
                current.next = new_node
                break
            current = current.next
        current = head
        before = None
        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after
        head = before
        return head
