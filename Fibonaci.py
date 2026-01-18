
class Solutions:

    def fibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

s = Solutions()
print( s.fibonacci(5) )