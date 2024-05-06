# Date: 06-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        before = None
        current = head
        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after

        head = before
        current = head
        while current is not None and current.next is not None:
            after = current.next
            if current.val > after.val:
                current.next = after.next
            else:
                current = current.next
        before = None
        current = head
        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after
        return before
