from queue import Queue
from stack import  StaskLinkedList

#problem 1 : reversing a queue Q
def reversing_queue(q: Queue):
    stack = StaskLinkedList()

    while not q.is_empty():
        stack.push(q.dequeue())

    while not stack.is_empty():
        q.enqueue(stack.pop())


#problem 2 :  implement queue using 2 stack
class QueueFrom2Stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def is_empty(self):
        return len(self.stack1) <= 0

    def size(self):
        return len(self.stack1)

    def dequeue(self):
        if not self.is_empty():
            while not self.is_empty():
                self.stack2.append(self.stack1.pop())

            data = self.stack2.pop()

            if len(self.stack2) > 0:
                while len(self.stack2) > 0:
                    self.stack1.append(self.stack2.pop())

            return data

if __name__ == "__main__":
    queue = QueueFrom2Stacks()
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(8)
    print(queue.size())
    print("queue : %d" % queue.dequeue())
    print(queue.size())