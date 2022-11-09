"""
to reverse the digit take a variable temp initialized with 0 and keep adding the remainder in it
by multiplying it 10 and divide the original number by 10 before the next recursion call.
to check is_palindrome just check if number == reverse of it (digit reversed)
"""


class Reverse:
    def __init__(self, temp, n):
        self.temp = temp
        self.n = n

    def reverse_digit(self):
        if self.n == 0:
            return
        self.temp = self.temp * 10 + self.n % 10
        self.n = self.n // 10
        self.reverse_digit()
        return self.temp

    def is_palindrome(self):
        return self.n == self.reverse_digit()


R = Reverse(0, 242)
print(R.is_palindrome())
# print(R.reverse_digit())
