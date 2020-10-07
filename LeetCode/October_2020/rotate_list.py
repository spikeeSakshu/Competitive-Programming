'''

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
    Input: 1->2->3->4->5->NULL, k = 2
    Output: 4->5->1->2->3->NULL
    Explanation:
    rotate 1 steps to the right: 5->1->2->3->4->NULL
    rotate 2 steps to the right: 4->5->1->2->3->NULL
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        temp= head
        length= 0
        while temp!= None:
            temp= temp.next
            length+=1
        
        if length ==0 or length==1 or k==0:
            return head
        
        for i in range(k%length):
            node= head
            end= head
            while end.next.next!= None:
                end= end.next
            
            node= end.next
            end.next= None
            node.next= head
            head= node
            
        
        return head
        
            