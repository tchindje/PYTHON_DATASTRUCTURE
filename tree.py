from stack import StaskLinkedList
from queue import Queue


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None
        self.parent: BinaryTreeNode = None

    def is_null(self) -> bool:
        return self is None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_left(self):
        return self.left

    def set_left(self, left_node):
        self.left = left_node

    def get_right(self):
        return self.right

    def set_right(self, left_node):
        self.right = left_node

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent


class BinaryTree:
    def __init__(self, node: BinaryTreeNode = None):
        self.root: BinaryTreeNode = node
        if node:
            self.size = 1
        else:
            self.size = 0

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.get_size() <= 0

    def prefix(self, root: BinaryTreeNode, result: list):

        """
        :param root: root node of tree
        :param result : contain visiting node in prefix order.
         insert  node in prefix order (DLR : data, left node, right node)
        :return: nothing
        """
        curr: BinaryTreeNode = root

        if curr is None:
            # print("can not traverse empty tree.")
            return

        result.append(curr.get_data())
        print(curr.get_data())
        self.prefix(curr.get_left(), result)
        self.prefix(curr.get_right(), result)

    def prefix_iterative(self, root: BinaryTreeNode, result: list):

        if root is None:
            # print("can not traverse empty tree.")
            return

        stack = StaskLinkedList()
        stack.push(root)

        while not stack.is_empty():
            cur_node: BinaryTreeNode = stack.pop()
            result.append(cur_node.get_data())  # append data to result list

            if cur_node.get_left() is not None:
                stack.push(cur_node.get_left())
            if cur_node.get_right() is not None:
                stack.push(cur_node.get_right())

    def infix(self, root: BinaryTreeNode, result: list):
        """

        :param root: root node of tree
        :param result : contain visiting node in infix order.
        insert  node in prefix order (LDR : left node,data, right node)
        :return: nothing

        """
        curr: BinaryTreeNode = root
        if curr is None:
            # print("can not traverse empty tree.")
            return

        self.infix(curr.get_left(), result)
        result.append(curr.get_data())
        self.infix(curr.get_right(), result)

    def infix_iterative(self, root: BinaryTreeNode, result: list):

        if root is None:
            # print("can not traverse empty tree.")
            return

        stack = StaskLinkedList()
        stack.push(root)

        while not stack.is_empty():

            cur_node: BinaryTreeNode = stack.pop()

            if cur_node.get_left() is not None:
                stack.push(cur_node.get_left())

            result.append(cur_node.get_data())  # append data to result list

            if cur_node.get_right() is not None:
                stack.push(cur_node.get_right())

    def postfix(self, root: BinaryTreeNode, result: list):
        """

        :param root: root node of tree
        :param result : contain visiting node in postfix order.
         insert  node in prefix order (LRD : left node, right node, data)
        :return: nothing

        """

        curr: BinaryTreeNode = root
        if curr is None:
            # print("can not traverse empty tree.")
            return

        self.postfix(curr.get_left(), result)
        self.postfix(curr.get_right(), result)
        result.append(curr.get_data())

    def postfix_iterative(self, root, result):
        if not root:
            return
        visited = set()
        stack = []
        node = root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.data)
                    node = None

    def level_order_traversal(self, root: BinaryTreeNode, result: list):
        if not root:
            return

            # using queue to enfile element at level l+1 when we  visiting element at level l
        queue = Queue()
        queue.enqueue(root)
        while not queue.is_empty():
            curr_node: BinaryTreeNode = queue.dequeue()
            result.append(curr_node.get_data())
            if curr_node.get_left():
                queue.enqueue(curr_node.get_left())
            if curr_node.get_right():
                queue.enqueue(curr_node.get_right())

    def insertion(self, new_node: BinaryTreeNode):
        # check is tree is empty
        if self.root is None:
            self.root = new_node
            self.size += 1
            return

        # search where to insert new node
        pre_curr = None
        curr: BinaryTreeNode = self.root
        while curr is not None:
            pre_curr = curr
            if new_node.get_data() < curr.get_data():
                curr = curr.get_left()
            else:
                curr = curr.get_right()

        # set parent node
        new_node.set_parent(pre_curr)
        if new_node.get_data() < pre_curr.get_data():
            pre_curr.set_left(new_node)
        else:
            pre_curr.set_right(new_node)

        self.size += 1  # increase size of tree

    def insertion_from_list(self, l: list):
        for e in l:
            self.insertion(BinaryTreeNode(e))

    #find minimum node of given root node to start and return it
    def find_min(self, node:BinaryTreeNode):
        if not node:
            return None

        curr = node
        while curr.get_left():
            curr = curr.get_left()
        return curr

    def find_max(self, node:BinaryTreeNode):
        if not node:
            return None

        curr = node
        while curr.get_right():
            curr = curr.get_right()
        return curr

    def find(self, root: BinaryTreeNode, val):
        if not root:
            print("empty tree.")
            return False

        curr = root
        if curr.get_data() == val:
            return True
        elif val < curr.get_data():
            return self.find(curr.get_left(), val)
        else:
            return self.find(curr.get_right(), val)

    def find_iter(self,root: BinaryTreeNode, val):
        if not root:
            return False

        curr = root
        find = False
        while not find and curr:
            if curr.get_data() == val:
                find = True
            elif val < curr.get_data():
                curr = curr.get_left()
            else:
                curr = curr.get_right()

        return find

    def get_size(self):
        return self.size

    # problem 8 : reverse order traversal level
    def level_reverse_order_traversal(self, root: BinaryTreeNode, stack):
        if not root:
            return

        # using queue to enfile element at level l+1 when we  visiting element at level l
        queue = Queue()
        queue.enqueue(root)
        while not queue.is_empty():
            curr_node: BinaryTreeNode = queue.dequeue()
            stack.push(curr_node.get_data())
            if curr_node.get_right():
                queue.enqueue(curr_node.get_right())
            if curr_node.get_left():
                queue.enqueue(curr_node.get_left())

    def delete_tree(self, node: BinaryTreeNode):
        if node is None:
            return
        self.delete_tree(node.get_left())
        self.delete_tree(node.get_right())
        del node
        self.size -=1

    def height(self, node: BinaryTreeNode):
        if node is None:
            return 0
        return max(self.height(node.get_right()), self.height(node.get_left())) + 1


    # calculate the successor of one node in infixe traversing  and return this node
    def successor(self, node: BinaryTreeNode):
        if node.get_right():
            succ = self.find_min(node.get_right())
            return succ

        pre_node = node.get_parent()
        while pre_node and pre_node.get_right() == node:
            node = pre_node
            pre_node = pre_node.get_parent()

        return pre_node

    def predecessor(self, node: BinaryTreeNode):
        if node.get_left():
            succ = self.find_max(node.get_right())
            return succ

        pre_node = node.get_parent()
        while pre_node and pre_node.get_left() == node:
            node = pre_node
            pre_node = pre_node.get_parent()

        return pre_node

    def delete_element(self, node:BinaryTreeNode):

        if not node:
            return

        # if node is a leaf
        elif node.get_left() is None and node.get_right() is None:
            pre_node = node.get_parent()
            if pre_node.get_right() is node:
                pre_node.set_right(None)
            else:
                pre_node.set_left(None)

            self.delete_tree(node) #delete a leaf node

        elif node.get_left() and not node.get_right():
            max_node = self.find_max(node.get_left())
            node.set_data(max_node.get_data() ) #copy satelite data
            self.delete_element(max_node) # recursive call delete_element at that node

        else:
            min_node = self.find_min(node.get_right())
            # replace info of node with info of min_node and delete min_node
            node.set_data(min_node.get_data())
            self.delete_element(min_node)

    def number_of_leaves_node(self, root :BinaryTreeNode):
        if not root:
            return 0

            # using queue to enfile element at level l+1 when we  visiting element at level l
        queue = Queue()
        queue.enqueue(root)
        count = 0
        while not queue.is_empty():
            curr_node: BinaryTreeNode = queue.dequeue()

            if curr_node.get_left() is None and curr_node.get_right() is None:
                count +=1

            if curr_node.get_left():
                queue.enqueue(curr_node.get_left())
            if curr_node.get_right():
                queue.enqueue(curr_node.get_right())

        return count

    def number_of_full_node(self, root: BinaryTreeNode):
        if not root:
            return 0

            # using queue to enfile element at level l+1 when we  visiting element at level l
        queue = Queue()
        queue.enqueue(root)
        count = 0
        while not queue.is_empty():
            curr_node: BinaryTreeNode = queue.dequeue()

            if curr_node.get_left() and curr_node.get_right() :
                count += 1

            if curr_node.get_left():
                queue.enqueue(curr_node.get_left())
            if curr_node.get_right():
                queue.enqueue(curr_node.get_right())

        return count

if __name__ == "__main__":

    tree = BinaryTree()
    print("empty tree : ", tree.is_empty())

    data = [6, 3, 8, 7, 9]

    tree.insertion_from_list(data)

    print("size : %d" % tree.get_size())

    print(f"max : {tree.find_max(tree.root).get_data()} ")
    print(f"min : {tree.find_min(tree.root).get_data()} ")
    print(f"result of search : {tree.find_iter(tree.root, val=9)} ")
    print(f"height : {tree.height(tree.root)} ")
    print(f"succes root : {tree.successor(tree.root).get_data()}")

    l = []
    tree.infix(tree.root,l)
    print(l)

    max_node = tree.find_max(tree.root)
    print(f"pred max node : { tree.predecessor(max_node).get_data()}")

    tree.delete_element(max_node)
    print("size : %d" % tree.get_size())

    l =[]
    tree.infix(tree.root, l)
    print(l)
    print(f"Number of full nodes : {tree.number_of_full_node(tree.root)}")
    print(f"Number of leaves nodes : {tree.number_of_leaves_node(tree.root)}")




