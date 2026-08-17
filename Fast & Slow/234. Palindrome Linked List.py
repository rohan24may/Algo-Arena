class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: # pyright: ignore[reportUndefinedVariable]

        # Step 1: Find middle using slow and fast pointer
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # Step 2: Reverse the second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node


        # Step 3: Compare first half and reversed second half
        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next


        return True