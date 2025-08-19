class iterator:
    def __init__(self, max):
        self.max = max
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= self.max:
            current = self.counter
            self.counter += 1
            return current
        else:
            raise StopIteration


counter = iterator(10)
for number in counter:
    print(number)
