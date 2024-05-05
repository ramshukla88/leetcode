# Date: 05-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        pre = None
        current = head
        while current:
            if current.val == val:
                if pre is None:
                    head = current.next
                else:
                    pre.next = current.next
            else:
                pre = current
            current = current.next
        return head



