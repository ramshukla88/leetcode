# Date: 06-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        before = None
        current = head

        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after

        return before