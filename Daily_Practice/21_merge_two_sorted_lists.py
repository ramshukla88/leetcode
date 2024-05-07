# Date: 08-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        curr1 = list1
        curr2 = list2
        dummy = ListNode(0)
        head = dummy
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                new_node = ListNode(curr1.val)
                dummy.next = new_node
                dummy = new_node
                curr1 = curr1.next
            else:
                new_node = ListNode(curr2.val)
                dummy.next = new_node
                dummy = new_node
                curr2 = curr2.next
        if curr1 is not None:
            dummy.next = curr1
        if curr2 is not None:
            dummy.next = curr2
        return head.next
