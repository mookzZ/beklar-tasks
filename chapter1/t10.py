class Counter:
    def __init__(self):
        self.count = 0
        print("init: ", self.count)
    def increment(self):
        self.count += 1
        print(self.count)
    def decrement(self):
        self.count -= 1
        print(self.count)

counter = Counter()
counter.increment()
counter.decrement()