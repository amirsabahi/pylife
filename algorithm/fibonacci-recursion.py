class Fibonacci:
    calculation = 0
    def fib(self, n):
        self.calculation += 1
        print('calculations', self.calculation)
        if n < 2:
            return n
        return self.fib(n-1) + self.fib(n-2)

f = Fibonacci()
print(f.fib(30)) # 55