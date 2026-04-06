#Clone Linked List with Random Pointer 👉 Deep copy of linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

def copy_list(head):
    old_new = {}
    curr = head

    while curr:
        old_new[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        old_new[curr].next = old_new.get(curr.next)
        old_new[curr].random = old_new.get(curr.random)
        curr = curr.next

    return old_new[head]