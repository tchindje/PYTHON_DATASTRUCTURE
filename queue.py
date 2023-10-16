class Queue:
    def __init__(self, list_data = None):
        self.tab = []

        if list_data is not None :
            for e in list_data:
                self.enqueue(e)

    def size(self):
        return len(self.tab)

    def is_empty(self):
        return self.size() <= 0

    def enqueue(self, data):
        self.tab.insert(0, data)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Queue (queue underflow).")
        return self.tab.pop()

    def front(self):
        if self.is_empty():
            raise Exception("Empty Queue.")
        return self.tab[-1]


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next : Node = None
        self.prev : Node = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_next(self):
        return  self.next

    def set_next(self, node):
        self.next = node

    def get_previous(self):
        return self.prev

    def set_previous(self, node):
        self.prev = node


class QueueLinkedList:
    def __init__(self, list_data = None):
        self.rear: Node = None
        self.front : Node = None
        self.length = 0

        if list_data is not None:
            for e in list_data:
                self.enqueue(e)

    def size(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return  self.size() <= 0

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.rear = new_node
            self.front  = new_node
        else:
            new_node.set_next(self.rear)
            self.rear.set_previous(new_node)
            self.rear = new_node

        self.length +=1

    def frontt(self):
        if self.is_empty():
            raise Exception("empty queue")
        return self.front.get_data()

    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty queue")

        if self.length == 1: # just one element in queue
            data = self.front.get_data()
            self.rear = None
            self.front= None
            self.length -= 1
            return  data

        #save data front before update
        data = self.front.get_data()

        #update front pointer
        self.front = self.front.get_previous()
        self.front.set_next(None)
        self.length -= 1
        return data

    def display(self):
        if self.is_empty():
            print("empty queue. No element to listed")
        else:
            cur = self.rear
            result = []
            while cur is not None:
                result.append(cur.get_data())
                cur = cur.get_next()
            return  result


if __name__ == "__main__":
    queue = QueueLinkedList([9,5])
    # queue.enqueue(3)
    # queue.enqueue(4)
    print(queue)
    print(queue.is_empty())
    print(queue.frontt())
    print( "size: %d" % queue.size())
    print(queue.display())
    print(queue.dequeue())
    print(queue.display())
    print( "size: %d" % queue.size())


