from operator import le


class Queue:
    def __init__(self, queue_size):
        self.queue = [None] * queue_size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        count = 0
        for item in self.queue:
            if item == None:
                count += 1
        return count == len(self.queue)

    def is_full(self):
        count = 0
        for item in self.queue:
            if item != None:
                count += 1
        return count == len(self.queue)

    def peek(self):
        return self.queue[self.front]

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full!")
            return 
        self.front = 0
        self.rear += 1
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            self.front = -1
            self.rear = -1
            return
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        return item


if __name__ == "__main__":
    queue = Queue(5)
    print(queue.queue)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(1)
    
    print(queue.queue)
    print(len(queue.queue))

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.front, queue.rear)
    print(queue.queue)
    print(queue.is_empty())
        