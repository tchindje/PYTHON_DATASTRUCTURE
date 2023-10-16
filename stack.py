
class Stack :
    def __init__ (self, limit):
        self.stk = []
        self.limit = limit

    def is_empty(self) -> bool:
        return  self.size() <= 0

    def size(self) -> int:
        return len(self.stk)

    def is_full(self) -> bool:
        return  self.size() >= self.limit

    def push(self, data):
        if self.is_full():
            raise Exception("stack overflow")

        self.stk.append(data)

    def pop(self) :
        if self.is_empty():
            raise Exception("empty stack")

        return self.stk.pop()

    def top(self):
        if  self.is_empty() :
            raise Exception("empty stack")

        return self.stk[-1]

###########################################
class StackDoubling :
    def __init__(self, limit=1):
        self.stk = []
        self.limit = limit

    def is_empty(self) -> bool:
        return  self.size() <= 0

    def size(self) -> int:
        return len(self.stk)

    def resize(self) :
        self.limit = 2*self.limit

    def is_full(self) -> bool:
        return  self.size() >= self.limit

    def push(self, data):
        if self.is_full():
            print(f"doubing the limit of the stack. New  limit {2*self.limit}.")
            self.resize()

        self.stk.append(data)

    def pop(self) :
        if self.is_empty():
            raise Exception("empty stack")

        return self.stk.pop()

    def display(self) :
        print(self.stk)

    def top(self):
        if  self.is_empty() :
            raise Exception("empty stack")

        return self.stk[-1]


#############################################################
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next : Node = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_next(self):
        return  self.next


    def set_next(self, node):
        self.next = node


class StaskLinkedList:
    def __init__(self, list_data =None):
        self.head : Node = None
        self.lenght: int = 0

        if list_data is not None:
            for e in list_data:
                self.push(e)

    def is_empty (self) -> bool:
        return  self.lenght <= 0

    def push(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
        else:
            newNode.set_next(self.head)
            self.head = newNode
        self.lenght +=1

    def pop(self):
        if self.is_empty():
            raise Exception("Can't pop from empty stack")
        temp = self.head
        self.head = self.head.get_next()
        self.lenght -= 1

        return temp.get_data()

    def top(self):
        if self.is_empty():
            raise Exception("Empty stack.")

        return self.head.get_data()

    def size(self) -> int:
        return self.lenght

    def is_full(self):
        print("Stack implemented with linked list will never full unless memory overflow.")

    def display(self):
        if self.is_empty():
            return print("nothing to display. Empty stack.")

        temp = self.head
        result = []
        while temp is not None:
            result.append(temp.get_data())
            temp = temp.get_next()
        print(result)

#####################################################
class SmartStackGetMin:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def is_empty(self):
        return  len(self.stack) <= 0

    def push (self, d):
        if self.is_empty(): #stack is empty
            self.stack.append(d)
            self.min_stack.append(d)

        else:
            self.stack.append(d)
            if  self.get_min() < d : #using another stack more expensive in space complexity
                self.min_stack.append( self.get_min())
            else:
                self.min_stack.append(d)

    def pop(self):
        if self.is_empty() :
            raise Exception("empty stack")
        self.min_stack.pop()
        return self.stack.pop()

    def get_min(self):
        if self.is_empty():
            raise Exception("empty stack")

        return self.min_stack[-1]


# to solve problem 6
class SmartPlusStackGetMin:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def is_empty(self):
        return  len(self.stack) <= 0

    def push (self, d):
        if self.is_empty(): #stack is empty
            self.stack.append(d)
            self.min_stack.append(d)
        else:
            self.stack.append(d)
            if  d <= self.get_min():
                self.min_stack.append(d)

    def pop(self):
        if self.is_empty() :
            raise Exception("empty stack")

        x = self.stack.pop()
        if x <= self.get_min():
            self.min_stack.pop()

        return x

    def get_min(self):
        if self.is_empty():
            raise Exception("empty stack")

        return self.min_stack[-1]

