class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: # pyright: ignore[reportUndefinedVariable]

        slow = head
        fast = head

        # Phase 1: Detect cycle
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                # Phase 2: Find cycle starting node
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        # No cycle
        return None