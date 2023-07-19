class Solution(object):
    def isHappy(self, n):
        slow_runner = n
        fast_runner = self.get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = self.get_next(slow_runner)
            fast_runner = self.get_next(self.get_next(fast_runner))
        return fast_runner == 1

    def get_next(self, n):
        output = 0

        while n:
            digits = n % 10
            digits = digits ** 2
            output += digits
            n = n // 10
        return output
