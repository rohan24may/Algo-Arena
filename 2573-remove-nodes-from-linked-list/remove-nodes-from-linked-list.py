# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        while current:
            while stack and current.val > stack[-1].val:
                stack.pop()

            stack.append(current)
            current = current.next

        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]

        stack[-1].next = None

        return stack[0]