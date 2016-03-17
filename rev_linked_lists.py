"""Given the head node of a linked list, reverse the list and return as a new linked list.
Define in a function.

ex: 
ll_1 : three nodes: A > B > C > D
new_list = D > C > B > A

given: LinkedList class; Node class; no loops in original list

"""

def reverse_linked_list(ll_1):

    new_list = LinkedList(head = ll_1.head)

    curr = ll_1.head

    while curr.next != None:
        curr = curr.next
        new_node = curr
        new_node.next = new_list.head
        new_list.head = new_node
    
    return new_list



