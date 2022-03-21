from pip import main


class Stack:

    def __init__(self):
        self.top = -1
        self.stack = []

    def check_empty(self):
        return self.top == -1

    def push(self, item):
        self.stack.append(item)
        self.top += 1
        print("pushed item: " + item)

    def pop(self):
        if (self.check_empty()):
            return "stack is empty"
        pop_item = self.stack[self.top]
        self.stack = self.stack[:self.top]
        return pop_item


if __name__ == "__main__":
    stack = Stack()
    stack.push(str(1))
    stack.push(str(2))
    stack.push(str(3))
    print("poped item: " + stack.pop())
    print("stack after poping an element: " + ", ".join([x for x in stack.stack]))
    