class Stack:

    def __init__(self, k):
        self.top = -1
        self.size = k
        self.stack = [None] * k

    def check_empty(self):
        return self.top == -1

    def check_full(self):
        count = 0
        for item in self.stack:
            if item != None:
                count += 1
        return count == self.size

    def push(self, item):
        self.top += 1
        self.stack[self.top] = item
        print("pushed item: " + str(item))

    # incorrect algorithm
    def pop(self):
        if (self.check_empty()):
            return "stack is empty"
        pop_item = self.stack[self.top]
        self.stack = self.stack[:self.top]
        return pop_item


if __name__ == "__main__":
    stack = Stack(5)
    stack.push(str(1))
    stack.push(str(2))
    stack.push(str(3))
    print("poped item: " + stack.pop())
    print("stack after poping an element: " + ", ".join([x for x in stack.stack]))
    print(stack.stack)
