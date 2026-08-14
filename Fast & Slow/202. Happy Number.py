class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            total = 0

            while n > 0:
                digit = n % 10
                n //= 10
                total += digit * digit

            return total

        slow = n
        fast = get_next(n)

        while slow != 1:

            slow = get_next(slow)
            fast = get_next(get_next(fast))

            if slow == 1:
                return True

            if slow == fast:
                return False

        return True