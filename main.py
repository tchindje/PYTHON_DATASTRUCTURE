# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from stack import Stack, StackDoubling, StaskLinkedList

from palindrome import is_palindrome, is_palindrome_using_stack


def reverse_stack(stack, rev_stack):
    while not stack.is_empty():
        rev_stack.push(stack.pop())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stack = StaskLinkedList([8,9,0,2,6])
    reversed_stack = StaskLinkedList()

    reverse_stack(stack, reversed_stack)

    reversed_stack.display()

