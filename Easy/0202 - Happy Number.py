class Solution:
    def isHappy(self, n: int) -> bool:
        def square_sum(num):
            total_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = square_sum(n)

        return n == 1
