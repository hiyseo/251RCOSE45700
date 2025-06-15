class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    print("Top element:", s.peek())
    print("Popped:", s.pop())
    print("Stack size:", s.size())