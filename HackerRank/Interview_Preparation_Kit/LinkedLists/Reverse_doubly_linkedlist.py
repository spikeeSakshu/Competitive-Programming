'''
Code to reverse a doubly Linked List

Link: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
'''

def reverse(head):

    prev_node= None
    curr_node= head

    while curr_node!= None:
        prev_node= curr_node.prev
        curr_node.prev= curr_node.next
        curr_node.next= prev_node

        curr_node= curr_node.prev


    return prev_node.prev
