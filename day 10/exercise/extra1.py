class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b

        next_value = self.a + self.b
        self.a, self.b = self.b, next_value
        self.count += 1
        return next_value

if __name__ == "__main__":
    fib_iter = Fibonacci(10)
    for num in fib_iter:
        print(num)
