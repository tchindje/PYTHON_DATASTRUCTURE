from queue import Queue
from stack import StaskLinkedList
import  math


# problem 1 : reversing a queue Q
def reversing_queue(q: Queue):
    stack = StaskLinkedList()

    while not q.is_empty():
        stack.push(q.dequeue())

    while not stack.is_empty():
        q.enqueue(stack.pop())


# problem 2 :  implement queue using 2 stack
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


# problem 4 : sliding windows
def max_sum_sliding_window(A, w):

    num_slide = len(A) - w + 1
    print("num slide : ", num_slide)

    temp_max = - math.inf  # biggest number
    B = [None]*num_slide

    for i in range(num_slide):
        s = sum(A[i:i+w])
        B[i] = s
        if s > temp_max:
            temp_max = s

    return temp_max, B


if __name__ == "__main__":
    m, b = max_sum_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print("max sum in sliding window :  %d" % m)

