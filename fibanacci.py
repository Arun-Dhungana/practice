class Fibonacci:
    def __init__(self, limit):
        self.n = 1
        self.current = 1
        self.previous = -1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if 0 < self.n < 3:

            self.previous = self.previous + 1
            result = self.previous
            self.previous = 0
            self.n += 1
            return result

        elif 2 < self.n < self.limit:

            result = self.previous + self.current
            self.previous = self.current
            self.current = result
            self.n += 1
            return result

        else:
            raise StopIteration


fibonacci = iter(Fibonacci(12))
print(fibonacci)
while True:
    try:
        print(f"{next(fibonacci)}\n")
    except StopIteration:
        break
