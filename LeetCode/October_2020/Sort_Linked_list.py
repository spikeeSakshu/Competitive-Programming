'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        l, head_copy = [], head
        while head:
            l.append(head.val)
            head = head.next
        dummy = ListNode(0, head_copy)
        l.sort()
        for i in l:
            head_copy.val = i
            head_copy = head_copy.next
        return dummy.next