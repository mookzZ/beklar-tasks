class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def remove(self, item):
        self.items.remove(item)
    def check(self):
        print(self.items)

stack = Stack()
stack.push("Hello!")
stack.push("Watermelon")
stack.check()
stack.remove("Hello!")
stack.check()