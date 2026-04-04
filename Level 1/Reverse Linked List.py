class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


# input
arr = list(map(int, input().split()))

head = Node(arr[0])
temp = head

for x in arr[1:]:
    temp.next = Node(x)
    temp = temp.next

head = reverse(head)

# print
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next