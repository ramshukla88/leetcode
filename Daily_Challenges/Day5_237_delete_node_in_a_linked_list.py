# Date: 05-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node.next
        node.val = node.next.val
        node.next = node.next.next
        temp.next = None