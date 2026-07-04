class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:

        for i in range(num + 1):

            x = i
            rev = 0

            while x > 0:
                digit = x % 10
                rev = rev * 10 + digit
                x //= 10

            if i + rev == num:
                return True

        return False
        