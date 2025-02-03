class Fibonacci:
    cache = {}
    calculations = 0
    def fib(self, n):
        self.calculations += 1
        print('calculations', self.calculations)
        if n < 2:
            return n
        if n in self.cache:
            print('cache hit', n)
            return self.cache[n]
        self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]

f = Fibonacci()

print(f.fib(30))